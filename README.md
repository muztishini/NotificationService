добавления нового клиента в справочник со всеми его атрибутами:
POST /api/client
обновления данных атрибутов клиента:
PUT /api/client/{id}
удаления клиента из справочника:
DELETE /api/client/{id}
добавления новой рассылки со всеми её атрибутами:
POST /api/newsletter
получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам:
GEt /api/stat
получения детальной статистики отправленных сообщений по конкретной рассылке:
GEt /api/stat/{id}
обновления атрибутов рассылки:
PUT /api/newsletter/{id}
удаления рассылки:
DELETE /api/newsletter/{id}
обработки активных рассылок и отправки сообщений клиентам:
сообщения создаются при создании рассылки

документация по api/schema/swagger-ui/
                api/schema/redoc/
                