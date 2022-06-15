# Streamlit.io

Data visualization made easy, according to the creators. We shall see.

## Getting Started

This can be contained in a virtualenv later on, but [it seems][web] all we need
to start is the streamlit package itself.

    pip install streamlit
    streamlit hello

This launches a server for the [hello][lhd], [plotting][lpd], [animation][lad],
[mapping][lmd], and [dataframe][ldd] demos. Frankly, it's pretty impressive.

Then [documentation][doc] needs to be read, etc.

## Getting Started (For Real)

The [official install guide][ins] prefers virtual environments, and my go-to is
the `venv` module in Python 3.x (example here in Linux):

    python -m venv streamlit    # you may need to use python3 instead of python
    . streamlit/bin/activate    # on Windows: .\streamlit\Scripts\activate

Once that is done, you can install streamlit into the environment using `pip`:

    pip install streamlit       # streamlit prefers pipenv

Now streamlit should be available whenever you activate the `streamlit` venv as
shown above. Any streamlit script, e.g. `script.py`, can be run like so:

    streamlit run script.py

When you're done developing, remember to `deactivate` your virtual environment.
Other explorations will be in their own folder with their own README.md :)

[web]: https://streamlit.io
[doc]: https://docs.streamlit.io
[lhd]: http://localhost:8501
[lpd]: http://localhost:8501/Plotting_Demo
[lad]: http://localhost:8501/Animation_Demo
[lmd]: http://localhost:8501/Mapping_Demo
[ldd]: http://localhost:8501/DataFrame_Demo
[ins]: https://docs.streamlit.io/library/get-started/installation
