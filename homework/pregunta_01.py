# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

def load_data():
    # Ahora leemos de data/shipping-data.csv según indicaciones
    return pd.read_csv("data/shipping-data.csv")

def create_visual_for_shipping_per_warehouse(df):
    plt.figure()
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(
        title="Shipping per Warehouse",
        xlabel="Warehouse block",
        ylabel="Record Count",
        color="tab:blue",
        fontsize=8,
    )
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

def create_visual_for_mode_of_shipment(df):
    plt.figure()
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title="Mode of Shipment",
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"],
    )
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

def create_visual_for_average_customer_rating(df):
    plt.figure()
    stats = (
        df[["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe()
    )
    # Simplificamos columnas
    stats = stats["Customer_rating"][["min", "mean", "max"]]

    # Barra de rango
    plt.barh(
        y=stats.index,
        width=stats["max"] - 1,
        left=stats["min"],
        height=0.9,
        color="lightgray",
        alpha=0.8,
    )

    # Barra de valor medio
    colors = ["tab:green" if m >= 30 else "tab:orange" for m in stats["mean"]]
    plt.barh(
        y=stats.index,
        width=stats["mean"] - 1,
        left=stats["min"],
        height=0.5,
        color=colors,
        alpha=1.0,
    )

    plt.title("Average Customer Rating")
    ax = plt.gca()
    ax.spines["left"].set_color("gray")
    ax.spines["bottom"].set_color("gray")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

def create_visual_for_weight_distribution(df):
    plt.figure()
    df.Weight_in_gms.plot.hist(
        title="Shipped Weight Distribution",
        color="tab:orange",
        edgecolor="white",
    )
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.savefig("docs/weight_distribution.png")
    plt.close()

def write_dashboard_html():
    html = """<!DOCTYPE html>
<html>
  <body>
    <h1>Shipping Dashboard Example</h1>
    <div style="width:45%;float:left">
      <img src="shipping_per_warehouse.png" alt="Fig 1">
      <img src="mode_of_shipment.png" alt="Fig 2">
    </div>
    <div style="width:45%;float:left">
      <img src="average_customer_rating.png" alt="Fig 3">
      <img src="weight_distribution.png" alt="Fig 4">
    </div>
  </body>
</html>
"""
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    # 1) Crear carpeta docs si no existe
    os.makedirs("docs", exist_ok=True)

    # 2) Cargar datos
    df = load_data()

    # 3) Generar gráficos
    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)

    # 4) Escribir el HTML de dashboard
    write_dashboard_html()

if __name__ == "__main__":
    pregunta_01()