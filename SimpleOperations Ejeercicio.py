import functools

class SimpleOperations:
    # Método para aplicar un descuento al precio dado
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        return price * (1 - discount)

    # Método para calcular y agregar el impuesto al precio dado
    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        return price * (1 + tax_rate)

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
twenty_percent_discount = functools.partial(operations.apply_discount, discount=0.20)
vat_tax = functools.partial(operations.calculate_tax, tax_rate=0.21)  # 21% de impuesto

# Usar las funciones preconfiguradas.
price = 100
price_with_discount = twenty_percent_discount(price)
price_with_tax = vat_tax(price)

print("Precio con descuento del 20%:", price_with_discount)
print("Precio con impuesto del 21%:", price_with_tax)