import os, shutil
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Dict
import pandas as pd

NAMESPACES = {
    'cfdi': 'http://www.sat.gob.mx/cfd/4',
    'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'
}

def extract_data_from_xml(path: str) -> Dict:
    # Procesa un XML CFDI y devuelve un diccionario con los datos relevantes.
    tree = ET.parse(path)
    root = tree.getroot()
    
    emisor = root.find('cfdi:Emisor', NAMESPACES)
    receptor = root.find('cfdi:Receptor', NAMESPACES)
    timbre = root.find('.//tfd:TimbreFiscalDigital', NAMESPACES)
    concepto = root.find('cfdi:Conceptos/cfdi:Concepto', NAMESPACES)

    return {
        "ArchivoXML": os.path.basename(path),
        "NumeroFactura": root.get('Serie', '') + root.get('Folio', ''),
        "Fecha": root.get('Fecha'),
        "Total": float(root.get('Total', 0)),
        "Subtotal": float(root.get('SubTotal', 0)),
        "Moneda": root.get('Moneda', 'MXN'),
        "TipoComprobante": root.get('TipoDeComprobante'),
        "DescripcionConcepto": concepto.get('Descripcion') if concepto is not None else '',
        "EmisorRFC": emisor.get('Rfc') if emisor is not None else '',
        "EmisorNombre": emisor.get('Nombre') if emisor is not None else '',
        "ReceptorRFC": receptor.get('Rfc') if receptor is not None else '',
        "ReceptorNombre": receptor.get('Nombre') if receptor is not None else '',
        "ReceptorRegimenFiscal": receptor.get('RegimenFiscalReceptor') if receptor is not None else '',
        "UUID": timbre.get('UUID') if timbre is not None else '',
        "UsoCFDI": receptor.get('UsoCFDI') if receptor is not None else '',
        "MetodoPago": root.get('MetodoPago'),
        "FormaPago": root.get('FormaPago')
    }

def process_directory(xml_dir: str) -> str:
    #Procesa todos los XML en un directorio y genera un Excel.
    processed = []
    processed_dir = os.path.join(xml_dir, 'procesados_xml')
    os.makedirs(processed_dir, exist_ok=True)

    for file in os.listdir(xml_dir):
        if not file.lower().endswith('.xml'):
            continue
        path = os.path.join(xml_dir, file)
        try:
            data = extract_data_from_xml(path)
            processed.append(data)
            shutil.move(path, os.path.join(processed_dir, file))
        except Exception as e:
            print(f"⚠️ Error procesando {file}: {e}")

    df = pd.DataFrame(processed)
    if not df.empty:
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        df = df[df['Total'] > 1].sort_values('Fecha')
        excel_path = os.path.join(xml_dir, f"reporte_facturas_{datetime.now():%Y%m%d_%H%M%S}.xlsx")
        df.to_excel(excel_path, index=False)
        return f"✅ Procesadas {len(df)} facturas. Exportado a {excel_path}"
    return "⚠️ No se encontraron facturas válidas."
