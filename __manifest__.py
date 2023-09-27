{
   'name': "Seguimiento de Inmuebles",
    'description': """
    Este modulo permite al corredor administrar inmuebles y dar seguimiento a los interesados
    """,
    'depends': ['base'],
    'data': [
                'security/res.groups.xml',
                'security/ir.model.access.xml',
                'demo/inmuebles.xml',
                'demo/sg_tipo_inmueble.xml',
                'views/sg_inmueble.xml',

            ],
   'author': "Rodnie Montano Aguilera <montano.rodnie@saguapac.com.bo>"            
}