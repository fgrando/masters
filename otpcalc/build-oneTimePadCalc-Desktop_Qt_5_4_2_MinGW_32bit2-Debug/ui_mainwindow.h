/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.4.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout_2;
    QPushButton *pushButton;
    QGroupBox *groupBox;
    QGridLayout *gridLayout;
    QPushButton *PrevReplace;
    QLineEdit *lineEdit;
    QPushButton *NextReplace;
    QTextEdit *textEdit;
    QLabel *label;
    QWidget *widget;
    QHBoxLayout *horizontalLayout;
    QPushButton *Prev;
    QTextEdit *key;
    QPushButton *Next;
    QLabel *label_2;
    QMenuBar *menuBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1104, 418);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayout_2 = new QGridLayout(centralWidget);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setEnabled(false);
        pushButton->setMinimumSize(QSize(0, 46));

        gridLayout_2->addWidget(pushButton, 0, 0, 1, 1);

        groupBox = new QGroupBox(centralWidget);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        gridLayout = new QGridLayout(groupBox);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        PrevReplace = new QPushButton(groupBox);
        PrevReplace->setObjectName(QStringLiteral("PrevReplace"));
        PrevReplace->setMaximumSize(QSize(100, 16777215));

        gridLayout->addWidget(PrevReplace, 0, 0, 1, 1);

        lineEdit = new QLineEdit(groupBox);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setEnabled(true);
        lineEdit->setMaximumSize(QSize(100, 16777215));
        lineEdit->setMaxLength(1);
        lineEdit->setFrame(false);
        lineEdit->setReadOnly(true);

        gridLayout->addWidget(lineEdit, 0, 1, 1, 1);

        NextReplace = new QPushButton(groupBox);
        NextReplace->setObjectName(QStringLiteral("NextReplace"));
        NextReplace->setMaximumSize(QSize(100, 16777215));

        gridLayout->addWidget(NextReplace, 0, 2, 1, 1);


        gridLayout_2->addWidget(groupBox, 0, 1, 1, 1);

        textEdit = new QTextEdit(centralWidget);
        textEdit->setObjectName(QStringLiteral("textEdit"));
        textEdit->setMinimumSize(QSize(730, 0));
        textEdit->setMaximumSize(QSize(16777215, 55));
        textEdit->setVerticalScrollBarPolicy(Qt::ScrollBarAsNeeded);
        textEdit->setHorizontalScrollBarPolicy(Qt::ScrollBarAsNeeded);
        textEdit->setReadOnly(true);

        gridLayout_2->addWidget(textEdit, 0, 2, 1, 1);

        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setMaximumSize(QSize(16777215, 20));

        gridLayout_2->addWidget(label, 1, 0, 1, 1);

        widget = new QWidget(centralWidget);
        widget->setObjectName(QStringLiteral("widget"));

        gridLayout_2->addWidget(widget, 4, 0, 1, 3);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        Prev = new QPushButton(centralWidget);
        Prev->setObjectName(QStringLiteral("Prev"));
        Prev->setMaximumSize(QSize(10, 16777215));

        horizontalLayout->addWidget(Prev);

        key = new QTextEdit(centralWidget);
        key->setObjectName(QStringLiteral("key"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(key->sizePolicy().hasHeightForWidth());
        key->setSizePolicy(sizePolicy);
        key->setMaximumSize(QSize(16777215, 25));
        QFont font;
        font.setFamily(QStringLiteral("Courier New"));
        font.setPointSize(8);
        font.setBold(false);
        font.setWeight(50);
        key->setFont(font);
        key->setInputMethodHints(Qt::ImhLatinOnly|Qt::ImhNoPredictiveText|Qt::ImhPreferLatin);
        key->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        key->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        key->setTabChangesFocus(true);
        key->setUndoRedoEnabled(false);
        key->setLineWrapMode(QTextEdit::FixedPixelWidth);
        key->setLineWrapColumnOrWidth(800);
        key->setOverwriteMode(false);

        horizontalLayout->addWidget(key);

        Next = new QPushButton(centralWidget);
        Next->setObjectName(QStringLiteral("Next"));
        Next->setMaximumSize(QSize(10, 16777215));

        horizontalLayout->addWidget(Next);


        gridLayout_2->addLayout(horizontalLayout, 2, 0, 1, 3);

        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setMaximumSize(QSize(16777215, 50));

        gridLayout_2->addWidget(label_2, 3, 0, 1, 2);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1104, 18));
        MainWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "OtpC - One Time Pad Calculator", 0));
        pushButton->setText(QApplication::translate("MainWindow", "Open File", 0));
        groupBox->setTitle(QApplication::translate("MainWindow", "Change some Key char here", 0));
        PrevReplace->setText(QApplication::translate("MainWindow", "Try &previous char", 0));
        PrevReplace->setShortcut(QApplication::translate("MainWindow", "Down", 0));
        NextReplace->setText(QApplication::translate("MainWindow", "Try &next char", 0));
        NextReplace->setShortcut(QApplication::translate("MainWindow", "Up", 0));
        textEdit->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Use <span style=\" font-weight:600;\">left</span> and <span style=\" font-weight:600;\">right</span> arrow keys to change the current <span style=\" font-weight:600;\">key char position. </span>Use <span style=\" font-weight:600;\">up</span> and <span style=\" font-weight:600;\">down</span> arrow keys to change the<span style=\" font-weight:600;\"> char in that position</span>.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#0000ff;\">T"
                        "he only field editable is the key field</span><span style=\" color:#0000ff;\">.</span> Below the key field there are the samples and the decoded text, obtained by the XOR of key (in key field) and the  sample (in sample field). Good luck!</p></body></html>", 0));
        label->setText(QApplication::translate("MainWindow", "Current key:", 0));
        Prev->setText(QApplication::translate("MainWindow", "<", 0));
        Prev->setShortcut(QApplication::translate("MainWindow", "Left", 0));
        key->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">keykeykeykeykeykeykeykeykeykeykeykeykeykey</p></body></html>", 0));
        Next->setText(QApplication::translate("MainWindow", ">", 0));
        Next->setShortcut(QApplication::translate("MainWindow", "Right", 0));
        label_2->setText(QApplication::translate("MainWindow", "Loaded samples:", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
