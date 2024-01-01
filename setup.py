import setuptools

__version__ ='0.0.0'

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

repo_name = 'Text_Summarization'
auth_name = 'omkarborhade98'
src_repo = 'textSummarizer'

setuptools.setup(
    name=src_repo,
    version=__version__,
    author=auth_name,
    description="Text Summarization package using NLP",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{auth_name}/{repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{auth_name}/{repo_name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)