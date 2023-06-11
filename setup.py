from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
long_description = None
# with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()
 
setup(
      name='xs_moniter', # 包名称
      packages=find_packages(exclude=['__pycache__']), # 需要处理的包目录
      version='0.1.0', # 版本
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python', 'Intended Audience :: Developers',
        #   'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.9',
      ],
      install_requires=['pynvml','textual'],
    #   scripts=['x_moniter.css'],
      entry_points={'console_scripts': ['xs-moniter=xs_moniter.xs_moniter:main']},
    #   package_data={'': ['*.json']},
      author='rhyx14', # 作者
      description='A nv GPU moniter', # 介绍
    #   long_description=long_description, # 长介绍，在pypi项目页显示
    #   long_description_content_type='text/markdown', # 长介绍使用的类型
    #   url='https://github.com/Rhyx14/secretary',
      license='MIT', # 协议
      python_requires='>=3.8'
    #   keywords='pimm source manager'  # 关键字 搜索用
    )