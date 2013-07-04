from __future__ import with_statement
__license__   = 'GPL v3'
__copyright__ = '2008, Kovid Goyal kovid@kovidgoyal.net'
__docformat__ = 'restructuredtext en'

'''
Conversion to EPUB.
'''
from calibre.utils.zipfile import ZipFile, ZIP_STORED

def rules(stylesheets):
    for s in stylesheets:
        if hasattr(s, 'cssText'):
            for r in s:
                if r.type == r.STYLE_RULE:
                    yield r

def initialize_container(path_to_container, opf_name='metadata.opf',
        extra_entries=[]):
    '''
    Create an empty EPUB document, with a default skeleton.
    '''    
    CONTAINER = u'''\
<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
   <rootfiles>
      <rootfile full-path="{0}" media-type="application/oebps-package+xml"/>
   </rootfiles>
</container>
    '''.format(opf_name).encode('utf-8')
    zf = ZipFile(path_to_container, 'w')
    zf.writestr('mimetype', 'application/epub+zip', compression=ZIP_STORED)
    zf.writestr('META-INF/', '', 0755)
    zf.writestr('META-INF/container.xml', CONTAINER)
    return zf

