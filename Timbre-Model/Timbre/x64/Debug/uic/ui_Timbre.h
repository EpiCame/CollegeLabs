/********************************************************************************
** Form generated from reading UI file 'Timbre.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TIMBRE_H
#define UI_TIMBRE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_TimbreClass
{
public:

    void setupUi(QWidget *TimbreClass)
    {
        if (TimbreClass->objectName().isEmpty())
            TimbreClass->setObjectName(QString::fromUtf8("TimbreClass"));
        TimbreClass->resize(600, 400);

        retranslateUi(TimbreClass);

        QMetaObject::connectSlotsByName(TimbreClass);
    } // setupUi

    void retranslateUi(QWidget *TimbreClass)
    {
        TimbreClass->setWindowTitle(QCoreApplication::translate("TimbreClass", "Timbre", nullptr));
    } // retranslateUi

};

namespace Ui {
    class TimbreClass: public Ui_TimbreClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TIMBRE_H
