FROM vizzuality/gef-environment:0.0.7

COPY requirements.txt /project/requirements.txt
RUN pip install -r /project/requirements.txt

COPY src /project/gefcore/script

USER $USER
