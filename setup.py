from setuptools import setup, find_packages

setup(name='chartpy',
      version='0.05',
      description='Chart library',
      author='Saeed Amen',
      author_email='saeed@cuemacro.com',
      license='Apache 2.0',
      keywords = ['pandas', 'chart', 'plot', 'plotly'],
      url = 'https://github.com/cuemacro/chartpy',
      packages = find_packages(),
      include_package_data = True,
      install_requires = ['pandas',
                          'matplotlib',
                          'twython',
                          'pytz',
                          'requests',
                          'numpy',
                          'plotly',
                          'cufflinks',
                          'bokeh'],
	  zip_safe=False)