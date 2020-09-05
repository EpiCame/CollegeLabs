#include "repo.h"

void repo::load_from_file() {
	ifstream f(this->file_name);
	if (!f.is_open())
		throw repo_exception("Cant open file!\n");
	string line;
	
	while (f >> line) {
		int i = 0;
		string elems[4];
		string aux;
		while (!line.empty()) {
			if (line.front() == ',') {
				line.erase(line.begin());
				elems[i++] = aux;
				aux.clear();
			}
			aux.push_back(line.front());
			line.erase(line.begin());
		}
		timbru tmb{ atoi(elems[0].c_str()), elems[1],atoi(elems[2].c_str()), elems[3], atoi(aux.c_str()) };
		try {
			this->add(tmb);
		}
		catch(repo_exception&){}
	}
	f.close();
};

void repo::add(const timbru& tmb) {
	for (const auto& tb : this->rep)
		if (tmb == tb)
			throw repo_exception("Duplicated id!\n");
	rep.push_back(tmb);
	write_to_file();
};

void repo::write_to_file() {
	ofstream g(this->file_name);
	if (!g.is_open())
		throw repo_exception("Cant open file!\n");
	g << "";
	for (const auto& tb : rep)
		g << tb.to_str() << '\n';
	g.close();
}

void repo::del(const timbru& tmb) {
	for (int i = 0; i < rep.size(); i++)
		if (rep[i] == tmb)
		{
			rep.erase(rep.begin() + i);
			write_to_file();
			return;
		}
	throw repo_exception("Can't delete!\n");
};