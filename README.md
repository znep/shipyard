shipyard
========

An open-sourced collection of docker images that probably don't merit their own git repo, but serve as building blocks or one-off utilities.

### Build

Build all images in this project:

    $ bin/build

Build a single image from this project, with support for specific versions:

    $ bin/build name[/x.x]

### Images

- [socrata/data](data): Basic data container
- [socrata/base](base): Base ubuntu image that establises a base set of patterns and tools for building other containers
- [socrata/java](java): Socrata/base image with Oracle Java installed
- [socrata/ruby](ruby): Alias for [socrata/ruby:2.1](ruby/2.1)
- [socrata/ruby:2.1](ruby/2.1): socrata/base image with Ruby 2.1.5
