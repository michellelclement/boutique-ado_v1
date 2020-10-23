from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    # Post handler for profile view
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    # Render order history on this page
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        # Delete profile when we render the profile
        # 'profile': profile,
        # Add below for rendering order history
        'orders': orders,
        # To stop update profile message including bag contents
        'on_profile_page': True
    }

    return render(request, template, context)
