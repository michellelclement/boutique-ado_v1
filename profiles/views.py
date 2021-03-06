from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Below for stopping non logged in from viewing logged in features of profile
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

from checkout.models import Order

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    # Post handler for profile view
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
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


# Order history
@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
