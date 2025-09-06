from django import template

register = template.Library()

@register.filter
def to_whatsapp(phone):
    """
    Badilisha namba kuwa WhatsApp international format
    """
    if not phone:
        return ""
    
    # Ondoa spaces na plus
    phone = phone.replace(" ", "").replace("+", "")
    
    # Ikiwa inaanza na 0 → badilisha kuwa 255...
    if phone.startswith("0"):
        phone = "255" + phone[1:]
    
    return phone

