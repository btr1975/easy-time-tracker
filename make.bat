@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 2.0.2
REM

SET option=%1

IF "%option%" == "" (
    GOTO BAD_OPTIONS
)

IF "%option%" == "all" (
    uv run black easy_time_tracker/
    uv run black tests/
    uv run complexipy
    uv run pylint easy_time_tracker\
    uv run mypy easy_time_tracker\
    uv run pytest --cov --cov-report=html -vvv
    uv run bandit -c pyproject.toml -r .
    uv export --no-dev --no-emit-project --no-editable > requirements.txt
    uv export --no-emit-project --no-editable > requirements-dev.txt
    GOTO END
)

IF "%option%" == "build" (
    uv build --wheel --sdist
    GOTO END
)

IF "%option%" == "coverage" (
    uv run pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%option%" == "pylint" (
    uv run pylint easy_time_tracker\
    GOTO END
)

IF "%option%" == "pytest" (
    uv run pytest --cov -vvv
    GOTO END
)

IF "%option%" == "format" (
    uv run black easy_time_tracker/
    uv run black tests/
    GOTO END
)

IF "%option%" == "check-security" (
    uv run bandit -c pyproject.toml -r .
    GOTO END
)

IF "%option%" == "mypy" (
    uv run mypy easy_time_tracker\
    GOTO END
)

IF "%option%" == "pip-export" (
    uv export --no-dev --no-emit-project --no-editable > requirements.txt
    uv export --no-emit-project --no-editable > requirements-dev.txt
    GOTO END
)

IF "%option%" == "gh-pages" (
    rmdir /s /q docs\source\code
    uv run sphinx-apidoc -o ./docs/source/code ./temporal_private
    uv run sphinx-build ./docs ./docs/gh-pages
    GOTO END
)

IF "%option%" == "complexipy" (
    uv run complexipy
    GOTO END
)

:OPTIONS
@ECHO make options
@ECHO     all             To run coverage, format, pylint, and check-vuln
@ECHO     build           To build a distribution
@ECHO     coverage        To run coverage and display ASCII and output to htmlcov
@ECHO     check-vuln      To check for vulnerabilities in the dependencies
@ECHO     check-security  To check for vulnerabilities in the code
@ECHO     format          To format the code with black
@ECHO     mypy            To run mypy
@ECHO     pylint          To run pylint
@ECHO     pytest          To run pytest with verbose option
@ECHO     pip-export      To export the requirements.txt and requirements-dev.txt
@ECHO     gh-pages  To create the GitHub pages
GOTO END

:BAD_OPTIONS
@ECHO Argument is missing
@ECHO Usage: make.bat option
@ECHO.
GOTO OPTIONS

:END
