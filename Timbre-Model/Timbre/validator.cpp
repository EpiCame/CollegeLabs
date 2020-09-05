#include "validator.h"


void validator::validate_tibru(const timbru& tb) {
	string err;
	if (tb.get_id() <= 0)
		err.append("Id invalid!\n");
	if (tb.get_nume().empty())
		err.append("Nume invalid!\n");
	if (tb.get_an() < 1000)
		err.append("An invalid!\n");
	if (tb.get_tara().empty())
		err.append("Tara invalida!\n");
	if (tb.get_pret() <= 0)
		err.append("Pret invalid!\n");
	if (err.empty())
		return;
	else
		throw valid_exception(err);
};