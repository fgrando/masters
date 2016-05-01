/********************************************************************************
** Form generated from reading UI file 'samplebox.ui'
**
** Created by: Qt User Interface Compiler version 5.4.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SAMPLEBOX_H
#define UI_SAMPLEBOX_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_sampleBox
{
public:
    QGridLayout *gridLayout;
    QTextEdit *decrypted;
    QTextEdit *encrypted;

    void setupUi(QWidget *sampleBox)
    {
        if (sampleBox->objectName().isEmpty())
            sampleBox->setObjectName(QStringLiteral("sampleBox"));
        sampleBox->resize(1521, 74);
        gridLayout = new QGridLayout(sampleBox);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        decrypted = new QTextEdit(sampleBox);
        decrypted->setObjectName(QStringLiteral("decrypted"));
        decrypted->setMaximumSize(QSize(16777215, 25));
        QFont font;
        font.setFamily(QStringLiteral("Courier New"));
        decrypted->setFont(font);
        decrypted->setInputMethodHints(Qt::ImhNone);
        decrypted->setFrameShape(QFrame::Box);
        decrypted->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        decrypted->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        decrypted->setUndoRedoEnabled(false);
        decrypted->setLineWrapMode(QTextEdit::NoWrap);
        decrypted->setReadOnly(true);
        decrypted->setTabStopWidth(800);

        gridLayout->addWidget(decrypted, 1, 0, 1, 1);

        encrypted = new QTextEdit(sampleBox);
        encrypted->setObjectName(QStringLiteral("encrypted"));
        encrypted->setEnabled(false);
        encrypted->setMaximumSize(QSize(16777215, 25));
        encrypted->setFont(font);
        encrypted->setFrameShape(QFrame::Box);
        encrypted->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        encrypted->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        encrypted->setUndoRedoEnabled(false);
        encrypted->setLineWrapMode(QTextEdit::NoWrap);
        encrypted->setTabStopWidth(800);

        gridLayout->addWidget(encrypted, 0, 0, 1, 1);


        retranslateUi(sampleBox);

        QMetaObject::connectSlotsByName(sampleBox);
    } // setupUi

    void retranslateUi(QWidget *sampleBox)
    {
        sampleBox->setWindowTitle(QApplication::translate("sampleBox", "Form", 0));
        decrypted->setPlaceholderText(QApplication::translate("sampleBox", "message", 0));
        encrypted->setPlaceholderText(QApplication::translate("sampleBox", "sample", 0));
    } // retranslateUi

};

namespace Ui {
    class sampleBox: public Ui_sampleBox {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SAMPLEBOX_H
