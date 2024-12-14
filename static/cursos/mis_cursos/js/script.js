function confirmarDesuscripcion(ticketId) {
    console.log('Desuscribirse clickeado para ticket ID:', ticketId);
    
    Swal.fire({
        title: '¿Estás seguro?',
        text: "¡Esta acción no se puede deshacer!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, desuscribirme'
    }).then((result) => {
        if (result.isConfirmed) {
            const form = document.getElementById(`desuscribir-form-${ticketId}`);
            if (form) {
                fetch(form.action, {
                    method: 'POST',
                    body: new FormData(form),
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        Swal.fire({
                            title: 'Desuscripción exitosa',
                            text: data.message,
                            icon: 'success',
                            confirmButtonText: 'OK'
                        }).then(() => {
                            window.location.href = misCursosUrl;
                        });
                    } else {
                        Swal.fire({
                            title: 'Error',
                            text: data.message,
                            icon: 'error',
                            confirmButtonText: 'OK'
                        });
                    }
                })
                .catch(error => {
                    console.error('Error al desuscribirse:', error);
                    Swal.fire({
                        title: 'Error',
                        text: 'Hubo un problema al procesar la desuscripción.',
                        icon: 'error',
                        confirmButtonText: 'OK'
                    });
                });
            } else {
                console.error(`Formulario con ID desuscribir-form-${ticketId} no encontrado.`);
            }
        }
    });
}