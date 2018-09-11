def save_profile(backend, strategy, details, response,
        user=None, *args, **kwargs):
    if backend.name == 'vk-oauth2':
        user.token = response['access_token']
        user.save()
