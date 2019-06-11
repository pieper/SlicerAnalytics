cmake_minimum_required(VERSION 3.5)

project(SlicerAnalytics)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/SlicerAnalytics")
set(EXTENSION_CATEGORY "Developer")
set(EXTENSION_CONTRIBUTORS "Steve Pieper (isomics, Inc.)")
set(EXTENSION_DESCRIPTION "This extension tracks what you are doing and reports it to Google.")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/SlicerAnalytics.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/SlicerAnalytics/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a space separated string, a list or 'NA' if any

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(Analytics)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
