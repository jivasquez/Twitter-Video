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
      install_requires=['django-nonrel', 'mongodb-engine',  'djangotoolbox', 'pymongo'],
      dependency_links = ["https://bitbucket.org/wkornewald/django-nonrel/get/be48c152abc6.tar.gz#egg=django-nonrel", "https://bitbucket.org/wkornewald/djangotoolbox/get/a8cdf61ba9c0.tar.gz#egg=djangotoolbox", "https://github.com/django-nonrel/mongodb-engine/tarball/master#egg=mongodb-engine" ],
      )