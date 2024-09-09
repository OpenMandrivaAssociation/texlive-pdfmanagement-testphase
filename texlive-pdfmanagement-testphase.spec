Name:		texlive-pdfmanagement-testphase
Version:	72182
Release:	1
Summary:	LaTeX PDF management testphase bundle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfmanagement-testphase
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfmanagement-testphase.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfmanagement-testphase.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfmanagement-testphase.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a temporary package, which is used during a test phase
to load the new PDF management code of LaTeX. The new PDF
management code offers backend-independent interfaces to
central PDF dictionaries, tools to create annotations, form
Xobjects, to embed files, and to handle PDF standards. The code
is provided, during a testphase, as an independent package to
allow users and package authors to safely test the code. At a
later stage it will be integrated into the LaTeX kernel (or in
parts into permanent support packages), and the current
testphase bundle will be removed.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pdfmanagement-testphase
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase
%doc %{_texmfdistdir}/doc/latex/pdfmanagement-testphase

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
