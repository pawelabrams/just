# just – your personal command line assistant

Do you sometimes wish you could run docker images with `just run instructions`? Or clone from github without having to type git@github.com... And was it a colon or a slash?

Just is here for you :)

Currently supported:

* `just install <package>` installs package(s) with `apt`. You can remove package(s) adding `-` to their name, as in `apt`. `sudo` might be a good idea. Other package managers soon!
* `just clone <owner>/<repo>` clones a github repository.
* `just clone <package>` clones your github repo. Config required in file `just`.

To use `just` without `./` you need to add it to your `PATH`.
