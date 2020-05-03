#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Warnings
Summary:	Test::Warnings - Test for warnings and the lack of them
Summary(pl.UTF-8):	Test::Warnings - testowanie pod kątem ostrzeżeń i ich braku
Name:		perl-Test-Warnings
Version:	0.030
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d30550a4898499daf351f9cf31602121
URL:		https://metacpan.org/release/Test-Warnings
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.94
BuildRequires:	perl-Test-Tester >= 0.108
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you've ever tried to use Test::NoWarnings to confirm there are no
warnings generated by your tests, combined with the convenience of
done_testing to not have to declare a test count, you'll have
discovered that these two features do not play well together, as the
test count will be calculated before the warnings test is run,
resulting in a TAP error.

This module is intended to be used as a drop-in replacement for
Test::NoWarnings: it also adds an extra test, but runs this test
before done_testing calculates the test count, rather than after. It
does this by hooking into done_testing as well as via an END block.
You can declare a plan, or not, and things will still Just Work.

%description -l pl.UTF-8
Przy próbie użycia Test::NoWarnings w celu upewnienia się, że testy
nie generują ostrzeżeń w połączeniu z wygodą done_testing, aby nie
trzeba było deklarować liczby testów, okazuje się, że udogodnienia te
nie współpracują dobrze ze sobą - liczba testów jest obliczana przed
uruchomieniem testu ostrzeżeń, czego wynikiem jest błąd TAP.

Ten moduł jest pomyślany jako zamiennik Test::Nowarnings - także
dodaje dodatkowy test, ale uruchamia go zanim done_testing obliczy
liczbę testów, a nie po tym. Robi to przez wstawienie w done_testing,
a także poprzez blok END. Można zadeklarować plan lub nie, a wszystko
będzie po prostu działać.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/Warnings.pm
%{_mandir}/man3/Test::Warnings.3pm*
%{_examplesdir}/%{name}-%{version}
