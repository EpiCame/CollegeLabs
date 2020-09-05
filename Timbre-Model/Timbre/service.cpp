#include "service.h"


void service::add(int id, string nume, int an, string tara, int pret) {
	timbru tb{ id, nume,an,tara,pret };
	valid.validate_tibru(tb);
	rep.add(tb);
};