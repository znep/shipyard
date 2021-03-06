socrata/ruby
============

socrata/base image with Ruby installed

### Usage

Most uses of the image will be via `FROM socrata/ruby:<version>` in a Dockerfile, nonetheless, you can run a Ruby container as follows:

    $ docker pull socrata/ruby:<version>

    # Launch shell in the container
    $ docker run --rm -t -i socrata/ruby:<version> bash

    # Bind mount a directory into the container and build or run something
    $ docker run --rm -t -i -v `pwd`:/opt/my_app socrata/ruby:<version> ruby my_app.rb


### Available versions

- `socrata/ruby` _alias for `socrata/ruby:2.1`_
- `socrata/ruby:2.1`
- `socrata/ruby:2.2`
- `socrata/ruby:2.3`
- `socrata/ruby:2.3.5`
- `socrata/ruby:2.3.6`
- `socrata/ruby:2.5.0`
- `socrata/ruby:2.5.3`
