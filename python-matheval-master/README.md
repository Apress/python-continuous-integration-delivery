python-matheval is the second example project for [my book in progress on Continuous Delivery](https://deploybook.com/).

It is a python-based web service that evaluates a tree of mathematical expresions. For example it turns the JSON tree

    ["*", ["+", 2, 3], 4]

which corresponds to (2 + 3) * 4, into the result, 20.

It is a flask application, packaged with [dh-virtualenv](https://github.com/spotify/dh-virtualenv), run by [gunicorn](http://gunicorn.org/) and controlled through systemd.
