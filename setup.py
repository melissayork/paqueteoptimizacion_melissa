from setuptools import setup, find_packages

setup(
       #
        name="paqueteoptimizacion_york", 
        version="0.1",
        author="MelissaYork",
        author_email="<melissayork_8@hotmail.com>",
        description="'Un paquete de Python para algoritmos de optimización univariables y multivariables'",
        packages=find_packages(),
        install_requires=[''], 
        
        keywords=['python', 'primer paquete'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)