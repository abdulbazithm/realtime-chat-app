from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message
from django.db.models import Q
from django.shortcuts import redirect

User = get_user_model()


@login_required
def user_list_view(request):
    users = User.objects.exclude(id=request.user.id)

    user_data = []

    for user in users:
        unread_count = Message.objects.filter(
            sender=user,
            receiver=request.user,
            is_read=False
        ).count()

        user_data.append({
            "user": user,
            "unread_count": unread_count
        })

    return render(request, "user_list.html", {
        "user_data": user_data
    })

@login_required
def chat_view(request, username):
    other_user = get_object_or_404(User, username=username)

    # Mark unread messages sent TO current user as read
    Message.objects.filter(
        sender=other_user,
        receiver=request.user,
        is_read=False
    ).update(is_read=True)
    

    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) |
        Q(sender=other_user, receiver=request.user)
    ).order_by("timestamp")

    return render(request, "chat.html", {
        "other_user": other_user,
        "messages": messages
    })


@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    # Only sender can delete
    if message.sender != request.user:
        return redirect("user_list")

    username = message.receiver.username

    message.delete()

    return redirect("chat", username=username)