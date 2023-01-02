# Citas Pasaporte Gobernación de Antioquia

Para pagar la primera parte del derecho de expedición o renovación del pasaporte se debe ingresar a esta [página de la Gobernación de Antioquia](https://sedeelectronica.antioquia.gov.co/pasaporte/user/pago/) la cual parece que aleatoriamente otorga un token o turno para ingresar al formulario de pago de esta primera parte. Si no se llena rapidamente este formulario y se da click para ir a la pasarela de pagos, se pierde el turno y se tiene que volver a intentar nuevamente.

Los intentos pueden ser muchos para lograr conseguir un turno. Por eso este script facilita la ejecución repetitiva de validación de la disponibilidad de un turno (osea si tenemos el formulario de solicitud de pago) para entonces llenar el formulario con la información del solicitante del pasaporte.

# Cómo usar?

1. Instalar Python
2. Instalar Selenium
3. Modificar los valores de las constantes  que incian con REQUESTER_ en el archivo [main.py](https://github.com/llanox/pasaporte_gobernacion_antioquia/blob/main/main.py) por los datos correspondientes a la del solicitante.
4. El valor de la constante URL_REQUEST_PAYMENT_FORM debe ser el de la constante URL_REAL. 
5. Ejecutar el script en el horario especificado en la página de la gobernación para el pago de la primera cita. Por lo general es apartir de las 8:00 am.

Notas
- En el momento de crear el script no tenia captcha alguno para validar el form. Entonces debería permitir redireccionar hasta la pasarela de pago sin intervención del usuario.
- El script solamente ha sido probado en Mac OSX Ventura 13.1 con Python 3.10
- En Mac OSX al estar disponible el formulario de pago se lee un texto (Text To Speech) para alertar el usuario que un formulario se va intentar dilegenciar. Para esto debe tener configurado configurada la voz Monica.




## License

[MPL-2.0](https://choosealicense.com/licenses/mpl-2.0/)
