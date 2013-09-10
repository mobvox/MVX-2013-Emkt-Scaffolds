# _*_ coding: utf-8 _*_

import common


class Files(object):
  """ HTML Scaffolding"""

  HTML = '''<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\">
  <title></title>
</head>
<body>
  <table cellspacing=\"0\" cellpadding=\"0\" width=\"100%%\" border=\"0\">
    %s<tr>
      <td align=\"center\">
        <table cellspacing=\"0\" cellpadding=\"0\" width=\"550\" border=\"0\">
          <tr>
            <td>
              
            </td>
          </tr>
        </table>
      </td>
    </tr>
    %s</table>
</body>
</html>'''

  ARCHIVE_MESSAGES = {
    'pt-BR': {
      'message': 'Caso n&atilde;o visualize este e-mail,',
      'link': 'clique aqui'
    },
    'en': {
      'message': 'If you cannot read the following message, please',
      'link': 'click here'
    },
    'es': {
      'message': 'Si usted no está viendo este mensaje,',
      'link': 'visite este enlace'
    }
  }

  UNSUB_MESSAGES = {
    'pt-BR': {
      'message': 'Caso não queira mais receber este email,',
      'link': 'desinscreva-se da lista'
    },
    'en': {
      'message': 'If you do not want to receive this email anymore',
      'link': 'unsubscribe from the list'
    },
    'es': {
      'message': 'Si no desea más recibir este email,',
      'link': 'visite este enlace'
    }
  }

  ARCHIVE_SNIPPET = '''<tr>
      <td
        height=\"50\" colspan=\"3\" align=\"center\"
        style=\"font-size: 12px; text-align: center; color: #575757; font-family: Arial, Helvetica, sans-serif;\">
        {message}
        <a href=\"*|ARCHIVE|*\" style=\"color: #575757; font-size: 12px; text-decoration: underline;\">{link}</a>.
      </td>
    </tr>
    '''
  UNSUB_SNIPPET = '''<tr>
      <td
        height=\"50\" colspan=\"3\" align=\"center\"
        style=\"font-size: 12px; text-align: center; color: #575757; font-family: Arial, Helvetica, sans-serif;\">
        {message}<a href=\"*|UNSUB|*\" style=\"color: #575757; font-size: 12px; text-decoration: underline;\">{link}</a>.
      </td>
    </tr>
    '''
  def getIndexHtmlData(self):
    return self.HTML % ('', '')

  def getEnvioHtmlData(self, lang='pt-BR'):
    return self.HTML % (self.ARCHIVE_SNIPPET.format(**self.ARCHIVE_MESSAGES[lang]),
      self.UNSUB_SNIPPET.format(**self.UNSUB_MESSAGES[lang]))

  def createProjectFiles(self, projectName='NewProject', langs=['pt-BR']):
    for lang in langs:
      if not lang in common.SUPPORTED_LANGS:
        raise KeyError('Unsupported language %s' % lang)
      index = '%s/%s/index.html' % (projectName, lang)
      envio = '%s/%s/envio.html' % (projectName, lang)
      with open(index, 'w') as f:
        print('Writing data to file %s' % index)
        f.write(self.getIndexHtmlData())
      with open(envio, 'w') as f:
        print('Writing data to file %s' % envio)
        f.write(self.getEnvioHtmlData(lang))


    