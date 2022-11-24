FROM python:3.11-bullseye
ARG USERNAME=django
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN apt-get update && \
  apt-get install -y sudo && \
  groupadd -g ${USER_GID} ${USERNAME} && \
  useradd -g $USER_GID -u ${USER_UID} -m -s '/bin/bash' ${USERNAME} && \
  echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
  chmod 0440 /etc/sudoers.d/$USERNAME

USER ${USERNAME}
WORKDIR /home/${USERNAME}
RUN echo 'export PATH=$HOME/.local/bin:$PATH' >> $HOME/.bashrc
RUN pip install --upgrade pip && \
  pip install --user pdm && \
  $HOME/.local/bin/pdm --pep582 bash >> $HOME/.bashrc && \
  mkdir -p __pypackages__

COPY --chown=$USERNAME . .
RUN $HOME/.local/bin/pdm sync --production
CMD ["/home/django/.local/bin/pdm", "run", "gunicorn", "mysite.wsgi"]
