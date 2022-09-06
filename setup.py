import setuptools

setuptools.setup(name='GrabYahooStock',
				version='0.2',
				description='Gets stock data from yahoo finance',
				url='#',
				author='me',
				install_requires=['requests', 'bs4', 'pandas'],
				author_email='',
				packages=setuptools.find_packages(),
				zip_safe=False)
