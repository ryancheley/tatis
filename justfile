# run tests via pytest, creates coverage report, and then opens it up
@test:
    coverage run -m pytest --cov-report html
    open htmlcov/index.html

# run the dev server
@run:
    python manage.py runserver

# deploys the code to the `target` server, which can be either an IP Address or alias to an IP
@deploy target: test
    @echo 'Deploying to {{target}}...'
    cd {{invocation_directory()}}/scripts; ./deploy.sh {{target}}

# prunes remote branches from github
@prune:
    git remote prune origin

# removes all but main and dev local branch
@gitclean:
    git branch | grep -v "main" | grep -v "dev"| xargs git branch -D

# runs mutation testing
@mutmut:
    @echo 'This may take a while ... got do something nice for yourself'
    mutmut run

# builds the styles.css into the static directory
@style-build:
    npx tailwindcss-cli@latest build jstoolchain/css/tailwind.css -c jstoolchain/tailwind.config.js -o static/css/styles.css

# builds the styles.css and deploys the css file
@style-deploy: style-build
    echo "not configured"

# checks the deployment for prod settings; will return error if the check doesn't pass
@settings:
    cp tatisjr/.env tatisjr/.env_staging
    cp tatisjr/.env_prod tatisjr/.env
    -python manage.py check --deploy
    cp tatisjr/.env_staging tatisjr/.env

# pulls from branch
@sync branch:
    git switch {{branch}}
    git pull origin {{branch}}

# runs the pre-commit check command
@check:
    pre-commit run --all-files


# install all needed packages and upgrade them too
@pip:
    pip install -U pip
    pip-compile --resolver=backtracking --quiet --upgrade --output-file requirements.txt
    pip install -r requirements.txt
