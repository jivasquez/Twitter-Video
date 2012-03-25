from setuptools import setup, find_packages


version = '0.1'

setup(name='twitter_video',
      version=version,
      description="WEB service que almacena y envía videos cortos",
      keywords='twitter videos cortos',
      author='Juan Ignacio Vasquez',
      author_email='ji.vasquez0@gmail.com',
      packages=['Twitter_video_web_service']
      include_package_data=True,
      zip_safe=False,
      install_requires=['']
      )