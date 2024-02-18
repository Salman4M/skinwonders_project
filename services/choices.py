from django.utils.translation import gettext_lazy as _


STATUS = (
    ('NEW IN',_('NEW IN')),
    ('LOW STOCK',_('LOW STOCK')),
)

SKINTYPE = (
    ('ALL',_('ALL')),
    ('SENSITIVE',_('SENSITIVE')),
    ('OILY',_('OILY')),
    ('ACNE',_('ACNE')),
    ('NORMAL',_('NORMAL')),
    ('DRY',_('DRY')),

)


RATINGS = (
    (1,'1 star'),
    (2,'2 stars'),
    (3,'3 stars'),
    (4,'4 stars'),
    (5,'5 stars'),

)


SUBJECTS = (
    ('GENERAL INQUIRY',_('GENERAL INQUIRY')),
    ('CUSTOMER SUPPORT',_('CUSTOMER SUPPORT')),
    ('FEEDBACK OR SUGGESTIONS',_('FEEDBACK OR SUGGESTIONS')),
    ('PARTNERSHIP OR COLLABORATIONS',_('PARTNERSHIP OR COLLABORATIONS')),
)


LOCATIONS = (
    ("BAKU",_("BAKU")),
    ("SYDNEY",_("SYDNEY")),
    ("ZURICH",_("ZURICH")),
    ("TOKYO",_("TOKYO")),
    ("SAN-FRANCISCO",_("SAN-FRANCISCO")),
)


DEPARTMENTS = (
    ('Product Development and Research',_('Product Development and Research',)),
    ('Marketing and Branding',_('Marketing and Branding')),
    ('Sales and Distribution',_('Sales and Distribution')),
    ("Finance and Administration",_("Finance and Administration")),
    ("Research and Analytics",_("Research and Analytics")),
    ("Creative and Design",_("Creative and Design")),
)

TYPE=(
    ('TOP TIPS',_('TOP TIPS')),
    ('NEW IN',_('NEW IN')),
    ('HOW TO',_('HOW TO')),
    ('MASKS',_('MASKS')),
    ('SUNCARE',_('SUNCARE')),
    ('BESTSELLERS',_('BESTSELLERS')),
)

DATE=(
    ('POPULAR',_('POPULAR')),
    ('RECENT',_('RECENT')),
)