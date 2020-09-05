#include "gui.h"
#include "repo.h"
#include "service.h"
#include "validator.h"

#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    validator valid;
    repo rep{ "timbre.txt" };
    service srv{ rep, valid };
    gui w{ srv };
    w.show();
    
    return a.exec();
}
