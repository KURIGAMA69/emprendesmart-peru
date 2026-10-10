
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EmprendeSmart Perú",
    page_icon="📈",
    layout="wide"
)

st.title("🚀 EmprendeSmart Perú")
st.subheader("Tu asistente inteligente para mejorar las ganancias de tu negocio")
st.write(
    "Simula escenarios, analiza tus costos y descubre "
    "oportunidades para hacer crecer tu emprendimiento."
)

st.divider()

st.sidebar.header("⚙️ Datos de tu negocio")

negocio = st.sidebar.text_input(
    "Nombre de tu negocio",
    "Mi emprendimiento"
)

ventas = st.sidebar.number_input(
    "Unidades vendidas al día",
    min_value=0,
    value=100,
    step=10
)

precio = st.sidebar.number_input(
    "Precio de venta por unidad (S/)",
    min_value=0.0,
    value=5.0,
    step=0.5
)

costo = st.sidebar.number_input(
    "Costo por unidad (S/)",
    min_value=0.0,
    value=2.5,
    step=0.5
)

gastos = st.sidebar.number_input(
    "Otros gastos diarios (S/)",
    min_value=0.0,
    value=30.0,
    step=5.0
)

dias = st.sidebar.number_input(
    "Días de trabajo al mes",
    min_value=1,
    max_value=31,
    value=26
)

ingresos = ventas * precio
costos_variables = ventas * costo
utilidad = ingresos - costos_variables - gastos
utilidad_mensual = utilidad * dias
margen = (utilidad / ingresos * 100) if ingresos > 0 else 0

st.header(f"📊 Panel de resultados: {negocio}")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Ventas diarias", f"S/ {ingresos:,.2f}")
c2.metric("Costos diarios", f"S/ {costos_variables + gastos:,.2f}")
c3.metric("Ganancia diaria", f"S/ {utilidad:,.2f}")
c4.metric("Ganancia mensual estimada", f"S/ {utilidad_mensual:,.2f}")

st.divider()

izquierda, derecha = st.columns(2)

with izquierda:
    st.subheader("📈 Proyección mensual")

    datos = pd.DataFrame({
        "Concepto": ["Ingresos", "Costos variables", "Otros gastos", "Ganancia"],
        "Monto (S/)": [
            ingresos * dias,
            costos_variables * dias,
            gastos * dias,
            utilidad_mensual
        ]
    })

    st.bar_chart(datos.set_index("Concepto"))

with derecha:
    st.subheader("💡 Diagnóstico empresarial")

    if utilidad < 0:
        st.error(
            "Tu negocio presenta pérdidas con estos datos. "
            "Revisa los costos y el precio de venta."
        )
        precio_equilibrio = costo + (gastos / ventas if ventas > 0 else 0)
        st.write(
            f"Precio aproximado por unidad para cubrir costos: "
            f"S/ {precio_equilibrio:.2f}"
        )
    elif utilidad == 0:
        st.warning(
            "Estás en el punto de equilibrio: tus ingresos "
            "cubren los costos registrados."
        )
    else:
        st.success(
            "Tu negocio genera una ganancia diaria positiva "
            "según los datos ingresados."
        )

    st.write(f"Margen de ganancia diario: {margen:.1f}%")

    if margen < 15 and ingresos > 0:
        st.info(
            "Oportunidad: analiza si puedes reducir costos "
            "o ajustar el precio sin perder clientes."
        )
    elif margen >= 15:
        st.info(
            "Siguiente reto: compara distintos precios y "
            "volúmenes de venta antes de tomar decisiones."
        )

st.divider()

st.header("🧪 Laboratorio de oportunidades")
st.write("Prueba qué ocurriría si aumentas tus ventas.")

aumento = st.slider(
    "Aumento de ventas esperado (%)",
    min_value=0,
    max_value=100,
    value=20,
    step=5
)

ventas_nuevas = ventas * (1 + aumento / 100)
ganancia_nueva = ventas_nuevas * (precio - costo) - gastos

a, b = st.columns(2)
a.metric("Unidades proyectadas al día", f"{ventas_nuevas:,.0f}")
b.metric(
    "Ganancia diaria proyectada",
    f"S/ {ganancia_nueva:,.2f}",
    delta=f"S/ {ganancia_nueva - utilidad:,.2f}"
)

st.caption(
    "Herramienta educativa de simulación. Los resultados son "
    "estimaciones basadas en los datos ingresados, no una "
    "garantía de ganancias."
)
