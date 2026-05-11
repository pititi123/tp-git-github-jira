import pandas as pd
import matplotlib.pyplot as plt

ventas = pd.read_csv('../datos/ventas.csv')

ventas['total'] = ventas['cantidad'] * ventas['precio']

ventas_totales = ventas['total'].sum()

producto_mas_vendido = ventas.groupby('producto')['cantidad'].sum().idxmax()

ventas['fecha'] = pd.to_datetime(ventas['fecha'])

ventas['mes'] = ventas['fecha'].dt.month

ventas_por_mes = ventas.groupby('mes')['total'].sum()

print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

print("\nVentas por mes:")
print(ventas_por_mes)

ventas_por_mes.plot(kind='bar')

plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.title('Ventas por Mes')

plt.savefig('../resultados/ventas_por_mes.png')

plt.show()