# SlidingWindowCounter

`SlidingWindowCounter` es una clase en Python que permite contar **usuarios únicos** en una ventana deslizante de tiempo (por defecto 5 minutos / 300 segundos). Es útil para procesar flujos de eventos en tiempo real, como clics de usuarios en una página web o interacciones en una aplicación.

## 📦 Descripción

La clase mantiene una cola (`deque`) de eventos ordenados por tiempo y un contador de usuarios (`defaultdict`) para llevar el registro de cuántas veces ha aparecido cada `user_id` dentro de la ventana de tiempo activa.

### Ejemplo de evento:

```python
{
  "timestamp": 1681500000,  # Unix timestamp (int)
  "user_id": "user_123"
}
