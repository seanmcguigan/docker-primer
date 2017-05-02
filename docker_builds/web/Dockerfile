#
# Super simple example of a Dockerfile
#
FROM ubuntu:latest
MAINTAINER Sean McGuigan

RUN apt-get update
RUN apt-get install -y python python-pip wget
RUN pip install Flask

ADD blog.py /home/blog.py
ADD templates/blog.html /home/templates/blog.html

WORKDIR /home

EXPOSE 5000

CMD ["blog.py"]

ENTRYPOINT ["python"]
