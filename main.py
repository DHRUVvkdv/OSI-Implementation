from layers.application_layer import ApplicationLayer
from layers.presentation_layer import PresentationLayer
from layers.session_layer import SessionLayer
from layers.transport_layer import TransportLayer
from layers.network_layer import NetworkLayer
from layers.data_link_layer import DataLinkLayer
from layers.physical_layer import PhysicalLayer

if __name__ == "__main__":
    data = "Test data to be sent through the OSI model."

    # Data flow from application layer down to physical layer
    app_layer = ApplicationLayer()
    presentation_layer = PresentationLayer()
    session_layer = SessionLayer()
    transport_layer = TransportLayer()
    network_layer = NetworkLayer()
    data_link_layer = DataLinkLayer()
    physical_layer = PhysicalLayer()

    app_layer.send(data)
    presentation_layer.send(data)
    session_layer.send(data)
    transport_layer.send(data)
    network_layer.send(data)
    data_link_layer.send(data)
    physical_layer.send(data)