from setuptools import setup


version = '0.1'

setup(name='twitter_video',
      version=version,
      description="WEB service que almacena y envia videos cortos",
      keywords='twitter videos cortos',
      author='Juan Ignacio Vasquez',
      author_email='ji.vasquez0@gmail.com',
      packages=['Twitter_video_web_service'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['django'],
      dependency_links = ["hg+https://bitbucket.org/wkornewald/django-nonrel", "hg+https://bitbucket.org/wkornewald/djangotoolbox", "git+https://github.com/django-nonrel/mongodb-engine" ],
      )