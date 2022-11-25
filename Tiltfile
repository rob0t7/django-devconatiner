# -*- mode: Python -*-

# allow_k8s_contexts('context')
# k8s_yaml(helm('helm', name='django-devcontainer'))
k8s_yaml(kustomize('./deployment'))
docker_build('django-devcontainer', '.', ignore=['helm', 'deployment'])
k8s_resource('django-devcontainer', port_forwards='8000:80', resource_deps=[])
k8s_resource('database', port_forwards='5432:5432')
local_resource('unittest', 'pdm test', deps=['mysite', 'polls'], labels=['Tests'])
local_resource('Lint', 'pdm run lint', deps=['mysite', 'polls'], labels=['Tests'])
