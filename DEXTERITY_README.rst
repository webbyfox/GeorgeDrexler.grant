**Congratulations!** If you're reading this document, you have created a Python
package meant to support development of Dexterity content types and behaviors.
This document introduces you to use of the package skeleton. *If you're using
templer.dexterity for the first time, you'll want to read every word.*

Adding the Package to Your Plone Installation
=============================================

You have probably created this package in a ./src subdirectory of your
buildout directory. If not, you may wish to move it there. The ./src
subdirectory is the expected place for development packages, and
development tools and documentation often assume this location.

Creating a development package does not automatically add the
package to your Plone runtime environment.

To do so, first find the
"eggs =" section of your buildout and add the name of
this package to your egg list::

    eggs =
        Plone
        Pillow
        lxml
        plone.app.dexterity
        ...
        georgedrexler.grant [test]

The `[test]` tells buildout to include testing support for
the package. That won't be needed for non-development use.

Next, you must tell buildout how to find the package. Otherwise, it would try
to download the package from a package repository. Look for the "develop ="
section of your buildout configuration file and add the path to this package::

    develop =
        src/georgedrexler.grant

Alternatively, you may use mr.developer to add the development package.

Now, run bin/buildout to integrate the new package into your runtime
environment. Restart zope/plone. Note that you should nearly always use
"foreground" mode when developing a package.

Adding Content Type and Behavior Skeletons
==========================================

You may use Templer and templer.dexterity to add content type or behavior
skeletons to your package. To do so, you must first integrate the new package
into your runtime environment (as described above) and run buildout. Without
that step, you will not be able to use the "add" command.

The "add" command allows for addition of "sub" skeletons like content types
and behaviors. It must be run inside the "src" directory of this package using
the "paster add" command.

To get a list of available add commands, do the following,
starting from your buildout directory::

    cd src/georgedrexler.grant/src
    ../../../bin/paster add --list

To add a new content type skeleton::

    cd src/georgedrexler.grant/src
    ../../../bin/paster add content_type

And, a behavior::

    cd src/georgedrexler.grant/src
    ../../../bin/paster add content_type

As when you ran templer to create this package, templer will ask you the
questions that must be answered to create the new skeleton.

Guide to The Package Skeleton
=============================

At the top level of your package (where this document) resides, you will find
the basic components of a distributable Python package. setup.py and setup.cfg
provide configuration of that package, and are frequently modified.

buildout.cfg may generally be ignored. It mainly exists to allow creation
of an environment for testing the templer.dexterity package. Feel free
to remove it. The same goes for bootstrap.py

Main documentation for your package is traditionally put in README.txt
at the top of the package. Supplementary documentation like history and
license files are typically located in the docs subdirectory.

The src subdirectory contains the source components of your package,
the working guts.

Inside the src directory, you will find a namespace directory,
georgedrexler, and inside that, the package heart: grant.

Inside src/georgedrexler/grant:

__init__.py
    Package initialization machinery. When you first create
    this package, it will contain some i18n setup.

locales : directory
    A directory for translations of your package messages.

profiles : directory
    Generic Setup profiles for this package

profiles/default : directory
    The default setup profile, often the only one. This will contain
    information on package dependencies and content type factory
    type information.

profiles/default/types.xml
    An empty Generic Setup content types list. List new types here.

profiles/default/metadata.xml
    Specify package dependencies and profile version number here.

static
    Use the static directory for non-template browser resources like images,
    stylesheets and JavaScript. See the README.txt in that directory.

configure.zcml
    Zope Control Markup Language directives for integrating this
    package and its zope components into the Zope runtime environment.
    This is a vital file, but if you only add content types and
    behaviors via "add" commands, you may be able to ignore it.
    The file is in XML.

INTEGRATION.txt
    A basic DocTest test file with a few simple tests. Add your
    own package integration tests here.

tests.py
    A test setup module. Since it's named "tests", it's automatically
    run by the test runner. When your package is first created, all
    this does is run the integration doc tests.

Guide to Content Type Skeletons
===============================

When you use the `add` local command to add a content-type skeleton,
it will create or modify the following files and directories:

content_class_templates : directory
    Put templates for your new type here

content_class_templates/sampleview.pt
    A sample view template for your new content type

models : directory
    One option for specifying your content type's field schema
    is to use a supermodel XML file. This is the place to put it.

models/content_class.xml
    An empty supermodel XML file for the content type. If you've
    been developing your content type TTW, you may export the
    model file and use it to replace this.

profiles/default/types.xml
    Your new type is automatically added to this type list.

profiles/default/types : directory
    If it didn't previously exist, this directory is created to
    contain factory-type information specifications for content
    types.

profiles/default/types/content_class.xml
    A plain vanilla Generic Setup factory-type information XML
    specification file. You'll nearly certainly edit this.

    One option for specifying your field schema is to download
    this file via the Dexterity control panel after specifying
    fields through-the-web.

content_class.py
    Add Python functionality here. This file contains a bare-bones
    interface definition, class declaration, and browser view class
    declaration (ties template to type).

    If you want to specify your field schema via Zope schema class
    attributes, do so here.

content_class.txt
    A sample DocTest file for your content type. Unless you've your
    own preferred testing mechanism, write tests for your content
    type functionality here.


Guide to Behavior Skeletons
===========================

Adding a behavior skeleton makes a smaller set of changes:

behavior_filename.py
    Create your behavior functionality here. This file contains
    the schema definitions and implementations for the behavior.

configure.zcml
    This file is altered to add the ZCML wiring to let Zope and
    Dexterity runtime know about your behavior.

Running Tests
=============

To run tests, you'll first need the Zope testrunner installed as
part of your buildout. If you've used the Unified Installer to set
up your buildout, that's included in the develop.cfg. If not, add::

    [test]
    recipe = zc.recipe.testrunner
    defaults = ['--auto-color', '--auto-progress']

    eggs =
        ${buildout:eggs}
        list of extra test-support packages

And add `[test]` to your parts list.

Run buildout to get the parts in place, then you'll be able to
run all your package tests with the command::

    bin/test -s georgedrexler.grant

Executed from your buildout directory.

Before Package Distribution or Deployment
=========================================

You should delete this file from your package before package distribution.
Failure to do so may result in your being ridiculed.

In order to support local "add" commands, Templer created Paste,
PasteDeploy and PasteScript eggs inside your product. These are only needed
for development. You can and should remove them from your add-on distribution.

Also remove::

  setup_requires=["PasteScript"],
  paster_plugins=["templer.localcommands"],

from the packages setup.py.
