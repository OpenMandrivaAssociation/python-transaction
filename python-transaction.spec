Name:		python-transaction
Version:	1.0.0
Release:	%mkrel 1
Group:		Development/Python
License:	Zope Public License
Summary:	Transaction management for Python
# md5=10b5d02dcded26f6f265771e6d68fc06
Source:		http://pypi.python.org/packages/source/t/transaction/transaction-1.0.0.tar.gz
URL:		http://pypi.python.org/pypi/transaction/1.0.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	python-devel
BuildRequires:	python-setuptools

%description
This package contains a generic transaction implementation for Python.
It is mainly used by the ZODB, though.

Note that the data manager API, transaction.interfaces.IDataManager,
is syntactically simple, but semantically complex. The semantics were
not easy to express in the interface. This could probably use more work.
The semantics are presented in detail through examples of a sample data
manager in transaction.tests.test_SampleDataManager.

%prep
%setup -q -n transaction-%{version}

%build

%install
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
