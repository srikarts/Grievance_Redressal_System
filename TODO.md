# TODO: Add OTP Validation for Registration Page

## Steps to Complete:
- [ ] Edit loginapp/forms.py: Add clean_email method to check email uniqueness.
- [ ] Edit loginapp/views.py: Add send_registration_otp view to generate and send OTP, and modify register_view to check OTP before saving user.
- [ ] Edit loginapp/urls.py: Add URL pattern for send_registration_otp.
- [ ] Edit loginapp/templates/loginapp/register.html: Add "Send OTP" button below email field, add hidden OTP input field, and add JavaScript for AJAX OTP sending and showing OTP field.
- [ ] Edit loginapp/static/loginapp/style1.css: Add CSS for OTP button and input field.
- [ ] Test the registration flow: Enter email, send OTP, enter OTP, submit form.
- [ ] Ensure emails are sent correctly (check settings for email backend).
- [ ] Handle edge cases like OTP expiry, invalid OTP, etc.
