import csv

from StringIO import StringIO

from trac.wiki.macros import WikiMacroBase
from trac.util.html import Markup
from trac.util import escape
from trac.wiki.api import parse_args

class CSV(WikiMacroBase):
    """Opens the CSV file and displays as an HTML table
    """
    
    # Render macro    
    def expand_macro(self, formatter, name, args):
        """
        """
        out = StringIO()
        
        path = parse_args(args)[0]
        
        if path[0]:
            content = open(path[0]).read()
            sniffer = csv.Sniffer()
            content = content.encode('utf-8', 'replace')
            reader = csv.reader(StringIO(content), sniffer.sniff(content))
            print >>out, '<table class="wiki">\n'
            for i, row in enumerate(reader):
                print >>out, '    <tr>\n'
                for col in row:
                    cellmarkup = '        <td>%s</td>\n'
                    if i == 0:
                        cellmarkup = '        <th>%s</th>\n'
                    print >>out, cellmarkup % escape(col)
                print >>out, '    </tr>\n'
            print >>out, '</table>'
        
        return Markup(out.getvalue())
