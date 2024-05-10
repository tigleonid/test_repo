## Подробный план четвертого модуля курса алгебры

### 6   Векторные пространства с ¯-билинейной формой

##### 6.1  ¯-Билинейные формы

-   Пр.-во билинейных форм:  $ \rm{Bi}(V) $ . Примеры билин. форм:  $ (v,w)\mapsto v^{\scriptscriptstyle\mathsf T}\!\cdot s\cdot w $  ( $ V=K^n $ ,  $ s\in\rm{Mat}(n,K) $ ),  $ (f,g)\mapsto\!\int_\alpha^\beta\!\!sfg $  ( $ V=\rm C^0\!([\alpha;\beta],\mathbb R) $ ,  $ s\in V $ ).

-   Поля с инволюцией. Пространство  $ \overline V $ :  $ c\overline\cdot v=\overline c\,v $ . Пространство ¯-билинейн. форм (полуторалинейных форм, если  $ \overline{\phantom c}\ne\rm{id}_K $ ):  $ \rm{\overline{Bi}}(V)=\rm{Bi}(V,\overline V,K) $ .

-   Матрица Грама формы  $ \sigma $ :  $ {(\sigma_{e,e})}_{j_1,j_2}\!=\sigma(e_{j_1}\!,e_{j_2}) $ . Обобщенная матрица Грама:  $ (\sigma_{(v_1,\ldots,v_m),(w_1,\ldots,w_m)})_{j_1,j_2}\!=\sigma(v_{j_1}\!,w_{j_2}) $ . Теорема о матрице Грама.

    **Теорема о матрице Грама.** *Пусть  $ K $  — поле с инволюцией,  $ V $  — векторное простр.-во над  $ K $ ,  $ n=\dim V<\infty $ ,  $ \sigma\in\rm{\overline{Bi}}(V) $  и  $ e\in\rm{OB}(V) $ ; тогда
    (1) для любых  $ v,w\in V $  выполнено  $ \sigma(v,w)=(v^e)^{\scriptscriptstyle\mathsf T}\!\cdot\sigma_{e,e}\!\cdot\overline{w^e}=\sum_{j_1=1}^n\sum_{j_2=1}^n\sigma_{j_1,j_2}v^{j_1}\overline{w^{j_2}} $  (координаты вычисляются относительно  $ e $ );
    (2) для любых  $ m\in\mathbb N_0 $  и  $ v_1,\ldots,v_m,w_1,\ldots,w_m\in V $  выполнено  $ \sigma_{(v_1,\ldots,v_m),(w_1,\ldots,w_m)}\!=\bigl(v_1^e\;\ldots\;v_m^e\bigr)^{\scriptscriptstyle\mathsf T}\!\cdot\sigma_{e,e}\!\cdot\overline{\bigl(w_1^e\;\ldots\;w_m^e\bigr)} $ .*

-   Изоморфизм вект. пр.-в  $ \biggl(\!\begin{align}\rm{\overline{Bi}}(V)&\to\rm{Mat}(n,K)\\\sigma&\mapsto\sigma_{e,e}\end{align}\!\biggr) $ . Преобразования при замене базиса:  $ \sigma_{\tilde e,\tilde e}=(\rm c_\tilde e^e)^{\scriptscriptstyle\mathsf T}\!\cdot\sigma_{e,e}\!\cdot\overline{\rm c_\tilde e^e} $  и  $ \sigma_{\tilde{j_1},\tilde{j_2}}\!=\sum_{l_1=1}^n\sum_{l_2=1}^n(e_\tilde{j_1})^{l_1}\overline{(e_\tilde{j_2})^{l_2}}\,\sigma_{l_1,l_2} $ .

-   Простр.-ва ¯-симметричных форм и матриц:  $ \rm{\overline{SBi}}(V)=\{\sigma\in\rm{\overline{Bi}}(V)\mid\forall\,v,w\in V\;\bigl(\sigma(w,v)=\overline{\sigma(v,w)}\bigr)\} $  и  $ \rm{\overline S}\rm{Mat}(n,K)=\{s\in\rm{Mat}(n,K)\mid s^{\scriptscriptstyle\mathsf T}\!=\overline s\} $ .

-   Пр.-ва ¯-антисимметр. форм и матриц:  $ \rm{\overline{ABi}}(V)=\{\sigma\in\rm{\overline{Bi}}(V)\mid\forall\,v,w\in V\;\bigl(\sigma(w,v)=-\overline{\sigma(v,w)}\bigr)\} $  и  $ \rm{\overline A}\rm{Mat}(n,K)=\{s\in\rm{Mat}(n,K)\mid s^{\scriptscriptstyle\mathsf T}\!=-\overline s\} $ .

-   Гомоморфизмы между простр.-вами с ¯-билинейной формой:  $ \rm{Hom}((V,\sigma),(Y,\varphi))=\{a\in\rm{Hom}(V,Y)\mid\forall\,v,w\in V\;\bigl(\sigma(v,w)=\varphi(a(v),a(w))\bigr)\} $ .

-   Изоморфизмы между пр.-вами с формой:  $ \rm{Iso}((V,\sigma),(Y,\varphi))=\rm{Hom}((V,\sigma),(Y,\varphi))\cap\rm{Bij}(V,Y) $  и  $ (V,\sigma)\cong(Y,\varphi)\,\Leftrightarrow\,\rm{Iso}((V,\sigma),(Y,\varphi))\ne\varnothing $ .

##### 6.2  ¯-Квадратичные формы

-   Пространство ¯-квадратичных форм:  $ \overline{\rm{Quad}}(V)=\{\kappa\in\rm{Func}(V,K)\mid\exists\,\sigma\in\overline{\rm{Bi}}(V)\;\forall\,v\in V\;\bigl(\kappa(v)=\sigma(v,v)\bigr)\} $ . Утверждение:  $ \kappa(c\,v)=c\,\overline c\,\kappa(v) $ .
-   ¯-Квадратичная форма  $ \kappa $  в коорд.:  $ \kappa(v)=(v^e)^{\scriptscriptstyle\mathsf T}\!\cdot\sigma_{e,e}\!\cdot\overline{v^e}=\sum_{j_1=1}^n\sum_{j_2=1}^n\sigma_{j_1,j_2}v^{j_1}\overline{v^{j_2}} $ ; если  $ \overline{\phantom c}=\rm{id}_K $ , то  $ \kappa(v) $  — однор. многочлен степени  $ 2 $  от  $ v^1,\ldots,v^n $ .
-   **Теорема о поляризации квадратичных форм.** *Пусть  $ K $  — поле,  $ \rm{char}\,K\ne2 $  и  $ V $  — векторное пространство над  $ K $ ; тогда
    (1) для любых  $ \kappa\in\rm{Quad}(V) $ , обозначая через  $ \,\rm{pol}_\kappa $  отображение  $ \biggl(\!\begin{align}V\times V&\to K\\(v,w)&\mapsto\bigl(\kappa(v+w)-\kappa(v)-\kappa(w)\bigr)/2\end{align}\!\biggr) $ , имеем следующие факты:
     $ \rm{pol}_\kappa $  — симметричная билинейная форма (то есть  $ \rm{pol}_\kappa\!\in\rm{SBi}(V) $ ), а также  $ \forall\,v\in V\;\bigl(\rm{pol}_\kappa(v,v)=\kappa(v)\bigr) $ ;
    (2) линейные операторы  $ \biggl(\!\begin{align}\rm{SBi}(V)&\to\rm{Quad}(V)\\\sigma&\mapsto\bigl(v\mapsto\sigma(v,v)\bigr)\!\end{align}\!\biggr) $  и  $ \biggl(\!\begin{align}\rm{Quad}(V)&\to\rm{SBi}(V)\\\kappa&\mapsto\rm{pol}_\kappa\end{align}\!\biggr) $  — взаимно обратные изоморфизмы векторных пространств.*
-   **Теорема о поляризации ¯-квадратичных форм над полем **C**.** *Пусть  $ V $  — векторное пространство над  $ \,\mathbb C $ ; тогда
    (1) для любых  $ \kappa\in\rm{\overline{Quad}}(V) $ , обозначая через  $ \,\rm{pol}_\kappa $  отображение  $ \biggl(\!\begin{align}V\times V&\to\mathbb C\\(v,w)&\mapsto\bigl(\kappa(v+w)+\rm i\,\kappa(v+\rm i\,w)-\kappa(v-w)-\rm i\,\kappa(v-\rm i\,w)\bigr)/4\end{align}\!\biggr) $ , имеем
    следующие факты:  $ \rm{pol}_\kappa $  — полуторалинейная форма (то есть  $ \rm{pol}_\kappa\!\in\rm{\overline{Bi}}(V) $ ), а также  $ \forall\,v\in V\;\bigl(\rm{pol}_\kappa(v,v)=\kappa(v)\bigr) $ ;
    (2) линейные операторы  $ \biggl(\!\begin{align}\overline{\rm{Bi}}(V)&\to\overline{\rm{Quad}}(V)\\\sigma&\mapsto\bigl(v\mapsto\sigma(v,v)\bigr)\!\end{align}\!\biggr) $  и  $ \biggl(\!\begin{align}\rm{\overline{Quad}}(V)&\to\rm{\overline{Bi}}(V)\\\kappa&\mapsto\rm{pol}_\kappa\end{align}\!\biggr) $  — взаимно обратные изоморфизмы векторных пространств.*
-   Гиперповерхность втор. порядка (аффинная квадрика) в  $ V $ : мн.-во вида  $ \{v\in V\mid\kappa(v)+2\,\lambda(v)+c=0\} $ , где  $ \kappa\in\rm{Quad}(V)\!\setminus\!\{0\} $ ,  $ \lambda\in V^* $  и  $ c\in K $ .
-   Примеры аффинных квадрик. Утверждение: *пусть  $ s\in\rm{Mat}(n,K) $ ,  $ \lambda\in K_n $ ,  $ c\in K $  и  $ v\in K^n $ ; тогда  $ \,v^{\scriptscriptstyle\mathsf T}\!\cdot s\cdot v+2\,\lambda\cdot v+c=\Bigl(\begin{smallmatrix}v\\1\end{smallmatrix}\Bigr)^{\!\scriptscriptstyle\mathsf T}\!\!\cdot\!\Bigl(\begin{smallmatrix}s&\lambda^{\scriptscriptstyle\mathsf T}\\\lambda&c\end{smallmatrix}\Bigr)\!\cdot\!\Bigl(\begin{smallmatrix}v\\1\end{smallmatrix}\Bigr) $ *.

##### 6.3  Музыкальные изоморфизмы и невырожденные ¯-билинейные формы

-   Оператор бемоль (опускание индекса):  $ \biggl(\!\begin{align}\flat_\sigma\colon V&\to\overline V^*\\v&\mapsto\bigl(w\mapsto\sigma(v,w)\bigr)\!\end{align}\!\biggr) $ . Опускание индекса в координатах:  $ (\flat_\sigma v)_e=(v^e)^{\scriptscriptstyle\mathsf T}\!\cdot\sigma_{e,e} $  и  $ (\flat_\sigma v)_j=\sum_{i=1}^nv^i\,\sigma_{i,j} $ .
-   Случай  $ \dim V<\infty $ :  $ \bigl( $  $ \sigma $  невырождена $ \bigr) $  $ \;\Leftrightarrow\; $  $ \bigl( $  $ \flat_\sigma $  — биекция $ \bigr) $  $ \;\Leftrightarrow\; $  $ \rm{Ker}\,\flat_\sigma\!=\{0\} $ . Ранг формы  $ \sigma $ :  $ \rm{rk}(\sigma)=\dim\rm{Im}\,\flat_\sigma $ . Утверждение:  $ \rm{rk}(\sigma)=\rm{rk}(\sigma_{e,e}) $ .
-   Топологическая невырожденность ( $ K=\mathbb R $  или  $ K=\mathbb C $ ,  $ V $  — нормир. пр.-во,  $ \sigma\in\overline{\rm{Bi}}(V)\cap\rm C^0\!(V\times V,K) $ ):  $ \biggl(\!\begin{align}\flat_\sigma\colon V&\to\overline V^*\!\!\cap\rm C^0\!(V,K)\\v&\mapsto\bigl(w\mapsto\sigma(v,w)\bigr)\!\end{align}\!\biggr) $  — биекция.
-   Пример:  $ K=\mathbb R $  или  $ K=\mathbb C $ ,  $ V=\ell^2_K=\bigl\{f\in\rm{Func}(\mathbb N,K)\mid\sum_{n=1}^\infty|f_i|^2\!<\infty\bigr\} $  и  $ \sigma\,\colon(f,g)\mapsto\sum_{i=1}^\infty f_i\overline{g_i} $ ; тогда  $ \sigma $  топологически невырожд. (без док.-ва).
-   Оператор диез (подъем индекса):  $ \sharp^\sigma\!=\flat_\sigma^{-1} $  ( $ \sigma $  невырождена). Подъем индекса в коорд. ( $ \sigma^{e,e}=(\sigma_{e,e}^{-1})^{\scriptscriptstyle\mathsf T} $ ):  $ (\sharp^\sigma\lambda)^e=\sigma^{e,e}\!\cdot(\lambda_e)^{\scriptscriptstyle\mathsf T} $  и  $ (\sharp^\sigma\lambda)^i=\sum_{j=1}^n\sigma^{i,j}\,\lambda_j $ .
-   **Теорема о базисах и невырожденных формах.** *Пусть  $ K $  — поле с инволюцией,  $ V $  — вект. простр.-во над  $ K $ ,  $ \sigma\in\rm{\overline{Bi}}(V) $ ,  $ m\in\mathbb N_0 $ ,  $ v_1,\ldots,v_m\in V $  и
     $ U=\langle v_1,\ldots,v_m\rangle $ ; тогда  $ \sigma_{(v_1,\ldots,v_m),(v_1,\ldots,v_m)}\!\in\rm{GL}(m,K) $ , если и только если  $ (v_1,\ldots,v_m)\in\rm{OB}(U) $  и форма  $ \sigma|_{U\times U} $  невырождена.*
-   Ортогональные векторы ( $ \sigma\in\rm{\overline{SBi}}(V)\cup\rm{\overline{ABi}}(V) $ ):  $ v\perp w\,\Leftrightarrow\,\sigma(v,w)=0\,\Leftrightarrow\,\sigma(w,v)=0 $ . Ортогональн. дополнение:  $ U^\perp\!=\{v\in V\mid U\perp v\}\le V $ .
-   **Теорема об ортогональном дополнении.** *Пусть  $ K $  — поле с инволюцией,  $ V $  — вект. простр.-во над  $ K $ ,  $ \sigma\in\rm{\overline{SBi}}(V)\cup\rm{\overline{ABi}}(V) $  и  $ U,W\le V $ ; тогда
    (1)  $ U\subseteq U^{\perp\perp} $ ,  $ U\subseteq W\,\Rightarrow\,W^\perp\!\subseteq U^\perp $ ,  $ (U+W)^\perp\!=U^\perp\!\cap W^\perp $  и  $ \,U^\perp\!+W^\perp\!\subseteq(U\cap W)^\perp $ ;
    (2) если  $ \dim V<\infty $  и форма  $ \sigma $  невырождена, то  $ \dim U^\perp\!=\dim V-\dim U $ , а также  $ U=U^{\perp\perp} $  и  $ \,U^\perp\!+W^\perp\!=(U\cap W)^\perp $ ;
    (3)  $ \rm{Ker}\bigl(\flat_{\sigma|_{U\times U}}\!\bigr)\!=U\cap U^\perp $  и, если  $ \dim U<\infty $ , то  $ \bigl( $ форма  $ \sigma|_{U\times U} $  невырождена $ \bigr) $  $ \;\Leftrightarrow\;\, $  $ U\cap U^\perp\!=\{0\} $ ;
    (4) если форма  $ \sigma|_{U\times U} $  невырождена, то  $ V=U\oplus U^\perp $  (и, значит, определен ортогональный проектор на  $ U $ :  $ \biggl(\!\begin{align}\rm{proj}_U\colon V=U\oplus U^\perp\!&\to V\\v=u+w&\mapsto u\end{align}\!\biggr) $ ).*

##### 6.4  Диагонализация ¯-симметричных ¯-билинейных форм

-   Ортогональный базис:  $ e\in\rm{OOB}(V,\sigma) $  $ \;\Leftrightarrow\; $  $ \bigl( $  $ \sigma_{e,e} $  — диагональная матрица $ \bigr) $ . Форма  $ \sigma $  в ортогональн. коорд. ( $ e\in\rm{OOB}(V,\sigma) $ ):  $ \sigma(v,w)=\sum_{i=1}^n\sigma_{i,i}\,v^i\overline{w^i} $ .

-   Ортонормированный базис ( $ K=\mathbb R $  или  $ K=\mathbb C $ ):  $ e\in\rm{OnOB}(V,\sigma) $  $ \;\Leftrightarrow\; $  $ \bigl( $  $ \sigma_{e,e} $  — диагональная матрица с  $ 1,\ldots,1,-1,\ldots,-1,0,\ldots,0 $  на диагонали $ \bigr) $ .

-   **Лемма о неизотропном векторе.** *Пусть  $ K $  — поле с инволюцией,  $ \rm{char}\,K\ne2 $ ,  $ V $  — вект. пр. над  $ K $  и  $ \sigma\in\rm{\overline{SBi}}(V)\!\setminus\!\{0\} $ ; тогда  $ \exists\,v\in V\;\bigl(\sigma(v,v)\ne0\bigr) $ .*

-   Теорема Лагранжа. Матричная формулировка теоремы Лагранжа. Алгоритм приведения квадратичной формы к сумме квадратов с коэффициентами.

    **Теорема Лагранжа.** *Пусть  $ K $  — поле с инволюцией,  $ \rm{char}\,K\ne2 $ ,  $ V $  — векторное пространство над  $ K $ ,  $ \dim V<\infty $  и  $ \sigma\in\rm{\overline{SBi}}(V) $ ; тогда
    (1) в пространстве  $ V $  существует ортогональный базис (то есть  $ \rm{OOB}(V,\sigma)\ne\varnothing $ );
    (2) если  $ K=\mathbb R $  или  $ K=\mathbb C $ , то в пространстве  $ V $  существует ортонормированный базис (то есть  $ \rm{OnOB}(V,\sigma)\ne\varnothing $ ).*

    **Матричная формулировка теоремы Лагранжа.** *Пусть  $ K $  — поле с инволюцией,  $ \rm{char}\,K\ne2 $ ,  $ n\in\mathbb N_0 $  и  $ s\in\rm{\overline S}\rm{Mat}(n,K) $ ; тогда
    (1) существует такая матрица  $ g\in\rm{GL}(n,K) $ , что  $ g^{\scriptscriptstyle\mathsf T}\!\cdot s\cdot\overline g $  — диагональная матрица;
    (2) если  $ K=\mathbb R $  или  $ K=\mathbb C $ , то сущ.-т такая матрица  $ g\in\rm{GL}(n,K) $ , что  $ g^{\scriptscriptstyle\mathsf T}\!\cdot s\cdot\overline g $  — диаг. матрица с  $ 1,\ldots,1,-1,\ldots,-1,0,\ldots,0 $  на диагонали.*

-   **Лемма об ортогональном проекторе.** *Пусть  $ K $  — поле с инволюцией,  $ V $  — вект. пр.-во над  $ K $ ,  $ \sigma\in\rm{\overline{SBi}}(V) $ ,  $ U\le V $ ,  $ m=\dim U<\infty $ ,  $ e\in\rm{OB}(U) $ ,
    форма  $ \sigma|_{U\times U} $  невырождена и  $ v\in V $ ; тогда  $ \rm{proj}_U(v)^e=(\sigma|_{U\times U})^{e,e}\!\cdot\!\biggl(\begin{smallmatrix}\sigma(v,e_1)\\\vdots\\\sigma(v,e_m)\end{smallmatrix}\biggr) $  и, если  $ e\in\rm{OOB}(U,\sigma|_{U\times U}) $ , то  $ \rm{proj}_U(v)=\sum_{i=1}^m\frac{\sigma(v,e_i)}{\sigma(e_i,e_i)}\,e_i $ *.

-   **Лемма об определителе матрицы Грама.** *Пусть  $ K $  — поле с инволюцией,  $ V $  — векторное простр.-во над  $ K $ ,  $ \sigma\in\rm{\overline{SBi}}(V) $ ,  $ m\in\mathbb N $ ,  $ v_1,\ldots,v_m\in V $ ,
     $ U=\langle v_1,\ldots,v_{m-1}\rangle $ , форма  $ \sigma|_{U\times U} $  невырождена и  $ \hat v_m=v_m-\rm{proj}_U(v_m) $ ; тогда  $ \det\sigma_{(v_1,\ldots,v_m),(v_1,\ldots,v_m)}=\det\sigma_{(v_1,\ldots,v_{m-1}),(v_1,\ldots,v_{m-1})}\cdot\sigma(\hat v_m,\hat v_m) $ .*

-   **Процесс ортогонализации Грама--Шмидта.** *Пусть  $ K $  — поле с инволюцией,  $ V $  — векторное пространство над  $ K $ ,  $ n=\dim V<\infty $ ,  $ \sigma\in\rm{\overline{SBi}}(V) $  и
     $ e\in\rm{OB}(V) $ ; для любых  $ i\in\{0,\ldots,n\} $  обозначим через  $ V_i $  пространство  $ \langle e_1,\ldots,e_i\rangle $  и обозначим через  $ cm_i $   $ i $ -й угловой минор матрицы  $ \sigma_{e,e} $  (то
    есть  $ cm_i=\det\sigma_{(e_1,\ldots,e_i),(e_1,\ldots,e_i)} $ ). Пусть для любых  $ i\in\{1,\ldots,n-1\} $  форма  $ \sigma|_{V_i\times V_i} $  невырождена (это эквивалентно тому, что  $ cm_i\ne0 $ ); для
    любых  $ i\in\{1,\ldots,n\} $  обозначим через  $ \hat e_i $  вектор  $ e_i-\rm{proj}_{V_{i-1}}(e_i) $ . Тогда для любых  $ i\in\{1,\ldots,n\} $  выполнено  $ (\hat e_1,\dots,\hat e_i)\in\rm{OOB}(V_i,\sigma|_{V_i\times V_i}) $  и
     $ \sigma(\hat e_i,\hat e_i)=\frac{cm_i}{cm_{i-1}} $ , а также  $ \hat e_i=e_i-\sum_{j=1}^{i-1}\frac{\sigma(e_i,\hat e_j)}{\sigma(\hat e_j,\hat e_j)}\,\hat e_j $  (это индуктивная формула для нахождения векторов  $ \hat e_1,\ldots,\hat e_n $ ).*

-   Ортогонал. системы функций:  $ \cos(nx) $  и  $ \sin(nx) $  ( $ n\in\mathbb N $ ),  $ \rm e^{nx\,\rm i} $  ( $ n\in\mathbb Z $ ), многочлены Лежандра, Чебышёва, Эрмита (см. пункты 5--10 в § 4 части 2 в \[5\]).

### 7   Геометрия в векторных пространствах над  $ \mathbb R $  или  $ \mathbb C $ 

##### 7.1  Положительно и отрицательно определенные формы и сигнатура формы

-   Мн.-ва положительно и отрицательно определенных форм:  $ \rm{\overline{SBi}}_{>0}(V)=\{\sigma\in\rm{\overline{SBi}}(V)\mid\forall\,v\in V\!\setminus\!\{0\}\;\bigl(\sigma(v,v)>0\bigr)\} $  и  $ \rm{\overline{SBi}}_{<0}(V)=-\rm{\overline{SBi}}_{>0}(V) $ .
-   Мн.-ва полож. и отриц. опред. матриц:  $ \rm{\overline S}\rm{Mat}_{>0}(n,K)=\{s\in\rm{\overline S}\rm{Mat}(n,K)\mid\forall\,v\in K^n\!\setminus\!\{0\}\;\bigl(v^{\scriptscriptstyle\mathsf T}\!\cdot s\cdot\overline v>0\bigr)\} $  и  $ \rm{\overline S}\rm{Mat}_{<0}(n,K)=-\rm{\overline S}\rm{Mat}_{>0}(n,K){} $ .
-   **Следствия из теоремы об ортогональном дополнении и теоремы Лагранжа.** *Пусть  $ K=\mathbb R $  или  $ K=\mathbb C $ ,  $ V $  — вект. пр.-во над  $ K $  и  $ \sigma\in\rm{\overline{Bi}}(V) $ ; тогда
    (1) если  $ \sigma\in\rm{\overline{SBi}}_{>0}(V) $  и  $ U\le V $ , то  $ U\cap U^\perp\!=\{0\} $  и, если  $ \dim U<\infty $ , то форма  $ \sigma|_{U\times U} $  невырождена и  $ V=U\oplus U^\perp $ ;
    (2) если  $ n=\dim V<\infty $ , то  $ \sigma\in\rm{\overline{SBi}}_{>0}(V) $ , если и только если  $ \exists\,e\in\rm{OB}(V)\;\bigl(\sigma_{e,e}=\rm{id}_n\bigr) $ ;
    (3) если  $ n=\dim V<\infty $  и  $ e\in\rm{OB}(V) $ , то  $ \sigma\in\rm{\overline{SBi}}_{>0}(V) $ , если и только если  $ \exists\,g\in\rm{GL}(n,K)\;\bigl(\sigma_{e,e}=g^{\scriptscriptstyle\mathsf T}\!\cdot\overline g\bigr) $ .*
-   **Критерий Сильвестра.** *Пусть  $ K=\mathbb R $  или  $ K=\mathbb C $ ,  $ V $  — векторное пространство над  $ K $ ,  $ n=\dim V<\infty $ ,  $ \sigma\in\rm{\overline{SBi}}(V) $  и  $ e\in\rm{OB}(V) $ ; для любых
     $ i\in\{1,\ldots,n\} $  обозначим через  $ cm_i $   $ i $ -й угловой минор матрицы  $ \sigma_{e,e} $  (то есть  $ cm_i=\det\sigma_{(e_1,\ldots,e_i),(e_1,\ldots,e_i)} $ ); тогда
    (1)  $ \sigma\in\rm{\overline{SBi}}_{>0}(V) $ , если и только если  $ \forall\,i\in\{1,\ldots,n\}\;\bigl(cm_i>0\bigr) $ ;
    (2)  $ \sigma\in\rm{\overline{SBi}}_{<0}(V) $ , если и только если  $ \forall\,i\in\{1,\ldots,n\}\;\bigl((-1)^i\,cm_i>0\bigr) $ .*
-   Индексы инерции формы  $ \sigma $ :  $ \rm{ind}_{>0}(\sigma)=\max\{\dim U\mid U\le V\,\land\,\sigma|_{U\times U}\!\in\overline{\rm{SBi}}_{>0}(U)\} $  и  $ \rm{ind}_{<0}(\sigma)=\max\{\dim U\mid U\le V\,\land\,\sigma|_{U\times U}\!\in\overline{\rm{SBi}}_{<0}(U)\} $ .
-   **Закон инерции Сильвестра.** *Пусть  $ K=\mathbb R $  или  $ K=\mathbb C $ ,  $ V $  — векторное простр.-во над  $ K $ ,  $ n=\dim V<\infty $ ,  $ \sigma\in\rm{\overline{SBi}}(V) $  и  $ e\in\rm{OOB}(V,\sigma) $ ; тогда
    (1)  $ \rm{ind}_{>0}(\sigma)=|\{i\in\{1,\ldots,n\}\mid\sigma(e_i,e_i)>0\}| $  (и, значит, число  $ |\{i\in\{1,\ldots,n\}\mid\sigma(e_i,e_i)>0\}| $  не зависит от  $ e $ );
    (2)  $ \rm{ind}_{<0}(\sigma)=|\{i\in\{1,\ldots,n\}\mid\sigma(e_i,e_i)<0\}| $  (и, значит, число  $ |\{i\in\{1,\ldots,n\}\mid\sigma(e_i,e_i)<0\}| $  не зависит от  $ e $ );
    (3)  $ \rm{ind}_{>0}(\sigma)+\rm{ind}_{<0}(\sigma)=\rm{rk}(\sigma) $ .*
-   **Теорема о классификации пространств с формой.** *Пусть  $ K=\mathbb R $  или  $ K=\mathbb C $ ,  $ V,Y $  — вект. простр.-ва над  $ K $ ,  $ \dim V,\dim Y<\infty $ ,  $ \sigma\in\rm{\overline{SBi}}(V) $  и
     $ \varphi\in\rm{\overline{SBi}}(Y) $ ; тогда  $ (V,\sigma)\cong(Y,\varphi) $ , если и только если  $ \dim V=\dim Y $ ,  $ \rm{ind}_{>0}(\sigma)=\rm{ind}_{>0}(\varphi) $  и  $ \rm{ind}_{<0}(\sigma)=\rm{ind}_{<0}(\varphi) $ .*
-   Сигнатура формы  $ \sigma $ :  $ (\rm{ind}_{>0}(\sigma),\rm{ind}_{<0}(\sigma)) $  (или  $ \rm{ind}_{>0}(\sigma)-\rm{ind}_{<0}(\sigma) $ ). Исследование кривых и поверхностей второго порядка (см. § 2 главы VIII в \[1\]).

##### 7.2  Предгильбертовы пространства

-   Предгильбертово пространство — вект. пр.-во над  $ \mathbb R $  или  $ \mathbb C $  с полож. опред. формой. Обозн.-е формы:  $ (\,\mid\,) $ . Примеры:  $ (v\!\mid\!w)=v^{\scriptscriptstyle\mathsf T}\!\cdot\overline w $ ,  $ (f\!\mid\!g)=\!\int_\alpha^\beta\!\!f\,\overline g $ .

-   Евклидово $ \,/\, $ унитарное пр.-во — конечномерн. вект. пр.-во над  $ \mathbb R $  $ \,/\, $  $ \mathbb C $  с полож. опред. формой, то есть конечномерн. предгильбертово пр.-во над  $ \mathbb R $  $ \,/\, $  $ \mathbb C $ .

-   Норма:  $ \|v\|=\sqrt{(v\!\mid\!v)} $ . Утверждение: * $ v\ne0\,\Rightarrow\,\|v\|>0 $  и  $ \|c\,v\|=|c|\,\|v\| $ *. Гильбертово пространство — полное предгильбертово пр.-во. Пример:  $ \ell^2 $ .

-   **Теорема о свойствах нормы.** *Пусть  $ V $  — предгильбертово пространство; тогда
    (1) для любых  $ v,w\in V $  выполнено  $ |(v\!\mid\!w)|\le\|v\|\,\|w\| $  (это неравенство Коши--Буняковского--Шварца);
    (2) для любых  $ v,w\in V $  выполнено  $ \|v+w\|\le\|v\|+\|w\| $  (это неравенство треугольника);
    (3) если  $ \dim V<\infty $ , то для любых  $ e\in\rm{OnOB}(V) $  и  $ v\in V $  выполнено  $ v=\!\sum_{i=1}^{\dim V}\!(v\!\mid\!e_i)\,e_i $  и  $ \|v\|^2=\!\sum_{i=1}^{\dim V}\!|(v\!\mid\!e_i)|^2 $  (это равенство Парсеваля).*

-   Метрика:  $ \rm{dist}(v,w)=\|v-w\| $ . Расстояние между подмн.-вами:  $ \rm{dist}(X,Y)=\inf\,\{\rm{dist}(x,y)\mid x\in X,\,y\in Y\} $ . Теорема о расстояниях и проекциях.

    **Теорема о расстояниях и проекциях.** *Пусть  $ V $  — предгильбертово пространство и  $ U,U'\!\le V $ ; тогда
    (1) для любых  $ v,v'\!\in V $  выполнено  $ \rm{dist}(v+U,v'+U')=\rm{dist}(v-v',U+U') $ ;
    (2) если  $ \dim U<\infty $ , то для любых  $ v\in V $  выполнено  $ \rm{dist}(v,U)=\rm{dist}(v,\rm{proj}_U(v)) $ ;
    (3) если  $ \dim V<\infty $ , то  $ \rm{proj}_U\!+\rm{proj}_{U^\perp}\!=\rm{id}_V $  и для любых  $ v\in V $  выполнено  $ \rm{dist}(v,U)=\|\rm{proj}_{U^\perp}\!(v)\| $ ;
    (4) если  $ \dim U<\infty $ , то для любых  $ e\in\rm{OnOB}(U) $  и  $ v\in V $  выполнено  $ \rm{proj}_U(v)=\!\sum_{i=1}^{\dim U}\!(v\!\mid\!e_i)\,e_i $  и  $ \|v\|^2\ge\!\sum_{i=1}^{\dim U}\!|(v\!\mid\!e_i)|^2 $  (это неравенство Бесселя).*

-   Метод наименьших квадратов: замена системы  $ a\cdot v=y $ , где  $ a\in\rm{Mat}(p,n,\mathbb R) $  и  $ \rm{rk}(a)=n $ , на систему  $ a\cdot v=\rm{proj}_X(y) $ , где  $ X=\{a\cdot v\mid v\in\mathbb R^n\} $ .

-   Угол между векторами и между вектором и подпр.-вом ( $ K=\mathbb R $ ,  $ v\ne0 $ ,  $ w\ne0 $ ,  $ U\ne\{0\} $ ):  $ \angle(v,w)=\arccos\frac{(v\!\mid\!w)}{\|v\|\,\|w\|}{} $  и  $ \angle(v,U)=\arccos\frac{\|\rm{proj}_U(v)\|}{\|v\|} $ .

-   Псевдоевклидово $ \,/\, $ псевдоунитарное пр.-во сигнатуры  $ (p,q) $  — кон.-мерн. вект. пр.-во над  $ \mathbb R $  $ \,/\, $  $ \mathbb C $  с невыр. ¯-симметр. ¯-билин. формой сигнатуры  $ (p,q) $ .

##### 7.3  Ориентация, объем, векторное произведение

-   Отн.-е одинак. ориентированности ( $ V $  — кон.-мерн. в. пр. над  $ \mathbb R $ ,  $ e,\tilde e\in\rm{OB}(V) $ ):  $ e\overset{\scriptscriptstyle\rm{or}}\sim\tilde e\,\Leftrightarrow\,\det\rm c_e^\tilde e\!>0 $ . Утверждение:  $ V\ne\{0\}\,\Rightarrow\,|\rm{OB}(V)/{\overset{\scriptscriptstyle\rm{or}}\sim}|=2 $ .

-   Ориентация пр.-ва  $ V $  — выбор эл.-та  $ \rm{OB}_{>0}(V) $  мн.-ва  $ \rm{OB}(V)/\overset{\scriptscriptstyle\rm{or}}\sim $ . Знак набора векторов:  $ \rm{sign}(v_1,\ldots,v_n) $ . Теорема о знаке базиса и формах объема.

    **Теорема о знаке базиса и формах объема.** *Пусть  $ V $  — векторное простр.-во с ориентацией и  $ e\in\rm{OB}(V) $ ; тогда для любых  $ \tilde e\in\rm{OB}(V) $  выполнено
     $ \rm{sign}(\tilde e)\,\rm{vol}^\tilde e\!=|\det\rm c_e^\tilde e|\,\rm{sign}(e)\,\rm{vol}^e $ , а также множество  $ \rm{VF}_{>0}(V) $ , равное  $ \,\mathbb R_{>0}\,\rm{sign}(e)\,\rm{vol}^e $ , не зависит от выбора упорядоченного базиса  $ e $ .*

-   Каноническая форма объема в псевдоевкл. пр.-ве с ориентацией ( $ e\in\rm{OB}(V) $ ):  $ \rm{vol}=\rm{sign}(e)\sqrt{|\det\sigma_{e,e}|}\,\rm{vol}^e $ ; если  $ e\in\rm{OnOB}_{>0}(V) $ , то  $ \rm{vol}=\rm{vol}^e $ .

-   Корректность опр.-я объема. Объем в коорд.:  $ \rm{vol}(v_1,\ldots,v_n)=\rm{sign}(e)\sqrt{|\det\sigma_{e,e}|}\!\!\!\sum_{1\le j_1,\ldots,j_n\le n}\!\!\!\varepsilon_{j_1,\ldots,j_n}v_1^{j_1}\!\cdot\ldots\cdot v_n^{j_n} $ . Лемма об объеме и матрице Грама.

    **Лемма об объеме и матрице Грама.** *Пусть  $ V $  — псевдоевклидово пространство сигнатуры  $ (p,q) $  с ориентацией,  $ n=p+q $  и  $ v_1,\ldots,v_n\in V $ ; тогда
    (1)  $ \rm{vol}(v_1,\ldots,v_n)=\rm{sign}(v_1,\ldots,v_n)\sqrt{|\det\sigma_{(v_1,\ldots,v_n),(v_1,\ldots,v_n)}|} $ ;
    (2) для любых  $ w_1,\ldots,w_n\in V $  выполнено  $ \rm{vol}(v_1,\ldots,v_n)\cdot\rm{vol}(w_1,\ldots,w_n)=(-1)^q\det\sigma_{(v_1,\ldots,v_n),(w_1,\ldots,w_n)} $ .*

-   Неотриц. объем в евкл. пр.-ве:  $ |\rm{vol}|_m(v_1,\ldots,v_m)=|\rm{vol}(v_1,\ldots,v_m)| $  в  $ \langle v_1,\ldots,v_m\rangle $ , если  $ v_1,\ldots,v_m $  независимы; иначе  $ |\rm{vol}|_m(v_1,\ldots,v_m)=0 $ .

-   **Теорема о неотрицательном объеме в евклидовом пространстве.** *Пусть  $ V $  — евклидово пространство,  $ m\in\mathbb N_0 $  и  $ v_1,\ldots,v_m\in V $ ; тогда
    (1)  $ |\rm{vol}|_m(v_1,\ldots,v_m)=\sqrt{\det\sigma_{(v_1,\ldots,v_m),(v_1,\ldots,v_m)}} $ ;
    (2) если  $ m\ge1 $  и  $ \hat v_m=v_m-\rm{proj}_{\langle v_1,\ldots,v_{m-1}\rangle}(v_m) $ , то  $ |\rm{vol}|_m(v_1,\ldots,v_m)=|\rm{vol}|_{m-1}(v_1,\ldots,v_{m-1})\cdot\|\hat v_m\| $ .*

-   Вект. произв. в псевдоевкл. пр.-ве с ориент.:  $ v_1\times\ldots\times v_{n-1}=\sharp\,\bigl(v_n\!\mapsto\rm{vol}(v_1,\ldots,v_n)\bigr) $  ( $ \Leftrightarrow\,\forall\,v_n\in V\;\bigl((v_1\times\ldots\times v_{n-1}\!\mid\!v_n)=\rm{vol}(v_1,\ldots,v_n)\bigr) $ ).

-   Векторное произведение в коорд.:  $ (v_1\times\ldots\times v_{n-1})^i=\rm{sign}(e)\sqrt{|\det\sigma_{e,e}|}\!\!\!\sum_{1\le j_1,\ldots,j_n\le n}\!\!\!\sigma^{i,j_n}\varepsilon_{j_1,\ldots,j_n}v_1^{j_1}\!\cdot\ldots\cdot v_{n-1}^{j_{n-1}} $ . Теорема о векторном произведении.

    **Теорема о векторном произведении.** *Пусть  $ V $  — псевдоевклидово пр.-во сигнатуры  $ (p,q) $  с ориентацией,  $ n=p+q\ge1 $  и  $ v_1,\ldots,v_{n-1}\in V $ ; тогда
    (1)  $ v_1\times\ldots\times v_{n-1}\in\langle v_1,\ldots,v_{n-1}\rangle^\perp $ , а также  $ v_1\times\ldots\times v_{n-1}\ne0 $ , если и только если векторы  $ v_1,\ldots,v_{n-1} $  независимы;
    (2) если  $ q=0 $ , то  $ \|v_1\times\ldots\times v_{n-1}\|=|\rm{vol}|_{n-1}(v_1,\ldots,v_{n-1}) $  и, если  $ v_1,\ldots,v_{n-1} $  независимы, то  $ (v_1,\ldots,v_{n-1},v_1\times\ldots\times v_{n-1})\in\rm{OB}_{>0}(V) $ ;
    (3) для любых  $ w_1,\ldots,w_{n-1}\in V $  выполнено  $ (v_1\times\ldots\times v_{n-1}\!\mid\!w_1\times\ldots\times w_{n-1})=(-1)^q\det\sigma_{(v_1,\ldots,v_{n-1}),(w_1,\ldots,w_{n-1})} $ ;
    (4) если  $ n=3 $  и  $ q=0 $ , то для любых  $ u,v,w\in V $  выполнено  $ (u\times v)\times w=(u\!\mid\!w)\,v-(v\!\mid\!w)\,u\, $  и  $ \,(u\times v)\times w+(v\times w)\times u+(w\times u)\times v=0 $ .*

##### 7.4  Автоморфизмы пространств с формой, ортогональные и унитарные операторы и матрицы

-   Группа автоморфизмов пр.-ва с ¯-билинейной формой:  $ \rm{Aut}(V,\sigma)=\rm{Iso}((V,\sigma),(V,\sigma))=\{a\in\rm{GL}(V)\mid\forall\,v,w\in V\;\bigl(\sigma(a(v),a(w))=\sigma(v,w)\bigr)\} $ .
-   Утверждение: *пусть  $ \rm{char}\,K\ne2 $  и  $ \sigma\in\rm{SBi}(V) $ , или  $ K=\mathbb C $  и  $ \sigma\in\rm{\overline{Bi}}(V) $ ; тогда  $ \,\rm{Aut}(V,\sigma)=\{a\in\rm{GL}(V)\mid\forall\,v\in V\;\bigl(\sigma(a(v),a(v))=\sigma(v,v)\bigr)\} $ *.
-   Ортогональная группа ( $ V $  — в. пр. над  $ \mathbb R $ ,  $ \sigma\in\rm{SBi}(V) $ ):  $ \rm O(V)=\rm{Aut}(V,\sigma) $ . Унитарная группа ( $ V $  — в. пр. над  $ \mathbb C $ ,  $ \sigma\in\rm{\overline{SBi}}(V) $ ):  $ \rm U(V)=\rm{Aut}(V,\sigma) $ .
-   **Лемма об автоморфизмах пространств с формой и матрицах.**
    *(1) Пусть  $ K $  — поле с инволюцией,  $ V $  — векторное пространство над  $ K $ ,  $ n=\dim V<\infty $ ,  $ \sigma\in\rm{\overline{Bi}}(V) $ ,  $ a\in\rm{End}(V) $  и  $ e\in\rm{OB}(V) $ ; тогда
     $ a\in\rm{Aut}(V,\sigma)\,\Leftrightarrow\,a_e^e\in\rm{GL}(n,K)\,\land\,(a_e^e)^{\scriptscriptstyle\mathsf T}\!\cdot\sigma_{e,e}\!\cdot\overline{a_e^e}=\sigma_{e,e} $  и, если форма  $ \sigma $  невырождена, то условие « $ \,a_e^e\in\rm{GL}(n,K) $ » можно убрать.
    (2) Пусть  $ V $  — псевдоевклидово пространство сигнатуры  $ (p,q) $  и  $ e,\tilde e\in\rm{OnOB}(V) $ ; тогда  $ (\rm c_\tilde e^e)^{\scriptscriptstyle\mathsf T}\!\cdot\!\Bigl(\begin{smallmatrix}\rm{id}_p&0\\0&-\rm{id}_q\end{smallmatrix}\Bigr)\!\cdot\rm c_\tilde e^e=\!\Bigl(\begin{smallmatrix}\rm{id}_p&0\\0&-\rm{id}_q\end{smallmatrix}\Bigr) $ .
    (3) Пусть  $ V $  — псевдоунитарное пространство сигнатуры  $ (p,q) $  и  $ e,\tilde e\in\rm{OnOB}(V) $ ; тогда  $ (\rm c_\tilde e^e)^{\scriptscriptstyle\mathsf T}\!\cdot\!\Bigl(\begin{smallmatrix}\rm{id}_p&0\\0&-\rm{id}_q\end{smallmatrix}\Bigr)\!\cdot\overline{\rm c_\tilde e^e}=\!\Bigl(\begin{smallmatrix}\rm{id}_p&0\\0&-\rm{id}_q\end{smallmatrix}\Bigr) $ .*
-   Матричные ортогонал. группы:  $ \rm O(p,q)=\{a\in\rm{Mat}(p+q,\mathbb R)\mid a^{\scriptscriptstyle\mathsf T}\!\cdot\!\Bigl(\begin{smallmatrix}\rm{id}_p&0\\0&-\rm{id}_q\end{smallmatrix}\Bigr)\!\cdot a=\!\Bigl(\begin{smallmatrix}\rm{id}_p&0\\0&-\rm{id}_q\end{smallmatrix}\Bigr)\} $ ,  $ \rm{SO}(p,q)=\rm{SL}(p+q,\mathbb R)\cap\rm O(p,q) $  и  $ \rm O(n) $ ,  $ \rm{SO}(n) $ .
-   Матричные унитарные группы:  $ \rm U(p,q)=\{a\in\rm{Mat}(p+q,\mathbb C)\mid a^{\scriptscriptstyle\mathsf T}\!\cdot\!\Bigl(\begin{smallmatrix}\rm{id}_p&0\\0&-\rm{id}_q\end{smallmatrix}\Bigr)\!\cdot\overline a=\!\Bigl(\begin{smallmatrix}\rm{id}_p&0\\0&-\rm{id}_q\end{smallmatrix}\Bigr)\} $ ,  $ \rm{SU}(p,q)=\rm{SL}(p+q,\mathbb C)\cap\rm U(p,q) $  и  $ \rm U(n) $ ,  $ \rm{SU}(n) $ .
-   Примеры:  $ \rm{SO}(2)=\bigl\{\Bigl(\begin{smallmatrix}\cos\varphi&-{\sin\varphi}\\\sin\varphi&\cos\varphi\end{smallmatrix}\Bigr)\!\mid\varphi\in[0;2\pi)\bigr\} $ ,  $ \rm O(2)=\rm{SO}(2)\cup\bigl\{\Bigl(\begin{smallmatrix}\cos\varphi&\sin\varphi\\\sin\varphi&-{\cos\varphi}\end{smallmatrix}\Bigr)\!\mid\varphi\in[0;2\pi)\bigr\} $  и  $ \rm{SU}(2)=\bigl\{\Bigl(\begin{smallmatrix}c&d\\-\overline d&\overline c\end{smallmatrix}\Bigr)\!\mid c,d\in\mathbb C,\,|c|^2\!+|d|^2\!=1\bigr\} $ .
-   **Теорема Эйлера о вращениях.** *Пусть  $ V $  — евклидово пр.-во с ориентацией,  $ \dim V=3 $  и  $ a\in\rm{SO}(V) $ ; тогда существуют такие  $ e\in\rm{OnOB}_{>0}(V) $  и
     $ \varphi\in[0;2\pi) $ , что  $ a_e^e=\biggl(\begin{smallmatrix}1&0&0\\0&\cos\varphi&-{\sin\varphi}\\0&\sin\varphi&\cos\varphi\end{smallmatrix}\biggr) $  (и, значит,  $ a $  — оператор поворота в  $ V $  на угол  $ \varphi $  против часовой стрелки вокруг оси с напр. вектором  $ e_1 $ ).*
-   Группа изометрий предгильбертова пр.-ва (как метрического пространства):  $ \rm{Isom}(V)=\{a\in\rm{Bij}(V)\mid\forall\,v,w\in V\;\bigl(\rm{dist}(a(v),a(w))=\rm{dist}(v,w)\bigr)\} $ .
-   **Теорема об описании изометрий.** *Пусть  $ V $  — предгильбертово пространство над  $ \,\mathbb R $ ; тогда  $ \{a\in\rm{Isom}(V)\mid a(0)=0\}=\rm O(V) $ , а также, обозначая
    через  $ G $ ,  $ F $  и  $ H $  группу  $ \,\rm{Isom}(V) $  и ее подгруппы  $ \{\bigl(v\mapsto v+z\bigr)\!\mid z\in V\} $  и  $ \{a\in\rm{Isom}(V)\mid a(0)=0\} $  соответственно, имеем следующие факты:
     $ F\cap H=\{\rm{id}_V\} $ ,  $ G=F\circ H $ ,  $ \forall\,h\in H\;\bigl(h\circ F\circ h^{-1}\!\subseteq F\bigr) $  и  $ F\cong V^+\! $  (и, значит,  $ \rm{Isom}(V)=\{\bigl(v\mapsto a(v)+z\bigr)\!\mid a\in\rm O(V),\,z\in V\}\cong V^+\!\leftthreetimes\rm O(V) $ ).*

##### 7.5  Тело кватернионов

-   Кольцо кватернионов:  $ \mathbb H=\{\alpha+\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k\mid\alpha,\beta,\gamma,\delta\in\mathbb R\} $ , где  $ \rm i^2=\rm j^2=\rm k^2=-1 $ , а также  $ \rm i\,\rm j=-\rm j\,\rm i=\rm k $ ,  $ \rm j\,\rm k=-\rm k\,\rm j=\rm i $  и  $ \rm k\,\rm i=-\rm i\,\rm k=\rm j $ .

-   Скалярная (вещественная) часть и векторная (мнимая) часть кватерниона:  $ \rm{Re}(\alpha+\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k)=\alpha $  и  $ \rm{Im}(\alpha+\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k)=\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k $ .

-   Пр.-во чистых кватернионов:  $ \mathbb H_\rm{vect}\!=\{v\in\mathbb H\mid\rm{Re}(v)=0\} $ . Скалярное произв.-е, векторное произв.-е, норма в  $ \mathbb H_\rm{vect} $ :  $ (v\!\mid\!w) $ ,  $ v\times w $ ,  $ \|v\|=\sqrt{(v\!\mid\!v)} $ .

-   Утверждение:  $ \forall\,v,w\in\mathbb H_\rm{vect}\,\bigl(v\,w=-(v\!\mid\!w)+v\times w\;\land\;v^2=-\|v\|^2\bigr) $ . Сопряжение:  $ \overline a=\rm{Re}(a)-\rm{Im}(a) $ . Модуль:  $ |a|=\sqrt{\rm{Re}(a)^2+\|\rm{Im}(a)\|^2} $ .

-   **Теорема о свойствах кватернионов.**
    *(1) Для любых  $ a\in\mathbb H $  выполнено  $ a\,\overline a=\overline a\,a=|a|^2 $  и, если  $ a\ne0 $ , то  $ a^{-1}\!=\!\frac{\overline a}{|a|^2} $  (и, значит,  $ \mathbb H $  — тело).
    (2) Для любых  $ a,b\in\mathbb H $  выполнено  $ \overline{a+b}=\overline a+\overline b $  и  $ \overline{a\,b}=\overline b\,\overline a $  (и, значит, отображение  $ \biggl(\!\begin{align}\mathbb H&\to\mathbb H\\a&\mapsto\overline a\end{align}\!\biggr) $  — антиавтоморфизм тела  $ \,\mathbb H $ ).
    (3) Для любых  $ a,b\in\mathbb H $  выполнено  $ |a\,b|=|a|\,|b| $  (и, значит, отображение  $ \biggl(\!\begin{align}\mathbb H^\times\!\!&\to\mathbb R_{>0}\!\\a&\mapsto|a|\end{align}\!\biggr) $  — гомоморфизм групп).*

-   Группа  $ \rm S^3 $ :  $ \rm S^3\!=\{g\in\mathbb H\mid|g|=1\} $ . Утверждение:  $ \mathbb H^\times\!\cong\mathbb R_{>0}\!\times\rm S^3 $ . Экспонента от кватерниона  $ a $ :  $ \rm e^a\!=\sum_{k=0}^\infty\frac1{k!}\,a^k $ . Теорема о свойствах экспоненты.

    **Теорема о свойствах экспоненты.**
    *(1) Для любых  $ a,b\in\mathbb H $  выполнено  $ a\,b=b\,a\,\Rightarrow\,\rm e^{a+b}\!=\rm e^a\!\cdot\rm e^b $ , а также  $ \rm e^0\!=1 $  и  $ \rm e^{-a}\!=(\rm e^a)^{-1} $ .
    (2) Для любых  $ \varphi\in\mathbb R $  и таких  $ u\in\mathbb H_\rm{vect} $ , что  $ \|u\|=1 $ , выполнено  $ \rm e^{\varphi\,u}\!=\cos\varphi+\sin\varphi\;u $  (и, значит,  $ \rm S^3\!=\{\rm e^{\varphi\,u}\!\mid\varphi\in[0;\pi],\,u\in\mathbb H_\rm{vect},\,\|u\|=1\} $ ).*

-   **Теорема об описании поворотов при помощи кватернионов.** *(1) Пусть  $ \varphi\in\mathbb R $ ,  $ u\in\mathbb H_\rm{vect} $  и  $ \|u\|=1 $ ; тогда  $ \biggl(\!\begin{align}\mathbb H_\rm{vect}\!&\to\mathbb H_\rm{vect}\\v&\mapsto\rm e^{\varphi\,u}\,v\,\rm e^{-\varphi\,u}\!\end{align}\!\biggr) $  — оператор
    поворота в пространстве  $ \,\mathbb H_\rm{vect} $  на угол  $ 2\varphi $  против часовой стрелки вокруг оси с направляющим вектором  $ u $ .
    (2) Отображение  $ \biggl(\!\begin{align}\rm S^3\!/\{1,-1\}&\to\rm{SO}(\mathbb H_\rm{vect})\\\{g,-g\}&\mapsto\bigl(v\mapsto g\,v\,g^{-1}\bigr)\!\end{align}\!\biggr) $  определено корректно и является изоморфизмом групп (и, значит,  $ \rm S^3\!/\{1,-1\}\cong\rm{SO}(3) $ ).*

### 8   Алгебры

##### 8.1  Определения и конструкции, связанные с алгебрами

-    $ K $ -Алгебра — вект. пространство над  $ K $  с билинейным умножением — кольцо в широком смысле слова с «правильным» умножением на скаляры из  $ K $ .

-   Примеры:  $ \rm{Func}(X,K) $ ,  $ K[x] $ ,  $ K(x) $ ,  $ \rm{Mat}(n,K) $ ,  $ \rm{End}(V) $ ;  $ \mathbb R $ -алгебры  $ \mathbb C $ ,  $ \mathbb H $ ,  $ \rm C^0\!(X,\mathbb R) $ ,  $ \rm C^\infty\!(M,\mathbb R) $ . Структурн. константы алгебры:  $ m^i_{j_1,j_2}\!\!=(e_{j_1}e_{j_2})^i $ .

-   Теорема Кэли для ассоциативных алгебр с  $ 1 $ . Инъект. гомоморфизмы  $ \mathbb R $ -алгебр:  $ \biggl(\!\begin{align}\mathbb C&\to\rm{Mat}(2,\mathbb R)\,\\\alpha+\beta\,\rm i&\mapsto\!\Bigl(\begin{smallmatrix}\alpha&-\beta\\\beta&\alpha\end{smallmatrix}\Bigr)\end{align}\!\biggr) $  и  $ \biggl(\!\begin{align}\mathbb H&\to\rm{Mat}(2,\mathbb C)\\\alpha+\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k&\mapsto\!\Bigl(\begin{smallmatrix}\alpha+\beta\,\rm i&\gamma+\delta\,\rm i\\-\gamma+\delta\,\rm i&\alpha-\beta\,\rm i\end{smallmatrix}\Bigr)\end{align}\!\biggr) $ .

    **Теорема Кэли для ассоциативных алгебр с 1.** *Пусть  $ K $  — поле и  $ A $  — ассоциативная  $ K $ -алгебра с  $ 1 $ ; обозначим через  $ {}_K\!A $  векторное пространство
    над  $ K $ , получающееся из  $ A $  при «забывании» умножения в этой алгебре, и для любых  $ a\in A $  обозначим через  $ \rm{lm}_a $  отображение  $ \biggl(\!\begin{align}A&\to A\\b&\mapsto a\,b\end{align}\!\biggr) $ ; тогда
    отобр.  $ \biggl(\!\begin{align}A&\to\rm{End}({}_K\!A)\\a&\mapsto\rm{lm}_a\end{align}\!\biggr) $  определено корректно и является инъективным гомоморфизмом алгебр с  $ 1 $  (и, значит,  $ A\cong\{\rm{lm}_a\!\mid a\in A\}\le\rm{End}({}_K\!A) $ ).*

-   Алгебра с делением:  $ \forall\,a\in A\!\setminus\!\{0\}\;\bigl(\rm{lm}_a,\rm{rm}_a\!\in\rm{Bij}(A)\bigr) $  и  $ A\ne\{0\} $ . Примеры:  $ K $ ,  $ K(x) $ ;  $ \mathbb R $ -алгебры с делением  $ \mathbb C $ ,  $ \mathbb H $ , алгебра октонионов (октав)  $ \mathbb O $ .

-   Моноидная алгебра ( $ M $  — моноид):  $ K[M]=\rm{FinFunc}(M,K) $ ; общий вид эл.-та:  $ \sum_{m\in M}p_mm $  ( $ |\{m\in M\mid p_m\ne0\}|<\infty $ ); умнож.-е в  $ K[M] $ : свертка.

-   Алгебра многочленов от свободных (некоммутирующих) перем.:  $ K\langle x_1,\ldots,x_n\rangle=K[\rm W(x_1,\ldots,x_n)] $ . Степень многочлена. Однородные многочлены.

-   Алгебра многочленов от коммутирующих переменных:  $ K[x_1,\ldots,x_n]=K[\rm W(x_1,\ldots,x_n)^\mathsf{ab}]\cong K\langle x_1,\ldots,x_n\rangle/\bigl(\{x_ix_j-x_jx_i\!\mid i,j\in\{1,\ldots,n\}\}\bigr) $ .

-   Алгебра многочленов от антикоммут. (грассмановых) перем.:  $ K_\wedge[x_1,\ldots,x_n]=K\langle x_1,\ldots,x_n\rangle/\bigl(\{x_ix_j+x_jx_i\!\mid i,j\in\{1,\ldots,n\}\}\cup\{x_1^2,\ldots,x_n^2\}\bigr) $ .

##### 8.2  Алгебры Ли (основные определения и примеры)

-    $ K $ -Алгебра Ли —  $ K $ -алгебра, умножение в которой антисимметрично ( $ [a,a]=0 $ ) и удовлетв.-т тождеству Якоби ( $ [[a,b],c]+[[b,c],a]+[[c,a],b]=0 $ ).

-   Коммутатор эл.-тов ассоциативной алгебры:  $ [a,b]=a\,b-b\,a $ . Алгебра  $ A^{(-)} $ : вект. простр.-во  $ {}_K\!A $  с операцией  $ [\,,] $ . Утверждение: * $ A^{(-)} $  — алгебра Ли*.

-   Примеры:  $ \mathfrak{gl}(V)=\rm{End}(V)^{(-)} $ ,  $ \mathfrak{sl}(V)=\{a\in\mathfrak{gl}(V)\mid\rm{tr}\,a=0\} $ , трехмерное евклид. пр.-во с ориент. относ.-но  $ \times $ ,  $ \mathbb H_\rm{vect} $  — подалгебра алгебры  $ \mathbb H^{(-)} $ .

-   Матричные алгебры Ли:  $ \mathfrak{gl}(n,K) $ ,  $ \mathfrak{sl}(n,K) $ ,  $ \mathfrak o(n)=\mathfrak{so}(n)=\{a\in\mathfrak{gl}(n,\mathbb R)\mid a^{\scriptscriptstyle\mathsf T}\!=-a\} $ ,  $ \mathfrak u(n)=\{a\in\mathfrak{gl}(n,\mathbb C)\mid a^{\scriptscriptstyle\mathsf T}\!=-\overline a\} $ ,  $ \mathfrak{su}(n)=\mathfrak{sl}(n,\mathbb C)\cap\mathfrak u(n){} $ .

-   **Теорема о группах матриц и матричных алгебрах Ли.** *Пусть  $ K=\mathbb R $  или  $ K=\mathbb C $  и  $ n\in\mathbb N_0 $ ; для любых  $ G\le\rm{GL}(n,K) $  обозначим через  $ \,\rm T_{\rm{id}_n}G $  мн.-во
     $ \{\dot\gamma(0)\mid\alpha\in[-\infty;0),\,\beta\in(0;\infty],\,\gamma\in\rm C^\infty\!((\alpha;\beta),\rm{Mat}(n,K)),\,\rm{Im}\,\gamma\subseteq G,\,\gamma(0)=\rm{id}_n\} $  (это касательное пр.-во к группе  $ G $  в точке  $ \,\rm{id}_n $ ); тогда
     $ \rm T_{\rm{id}_n}\rm{GL}(n,K)=\mathfrak{gl}(n,K) $  и  $ \,\rm T_{\rm{id}_n}\rm{SL}(n,K)=\mathfrak{sl}(n,K) $ , а также  $ \,\rm T_{\rm{id}_n}\rm O(n)=\rm T_{\rm{id}_n}\rm{SO}(n)=\mathfrak{so}(n) $ ,  $ \rm T_{\rm{id}_n}\rm U(n)=\mathfrak u(n) $  и  $ \,\rm T_{\rm{id}_n}\rm{SU}(n)=\mathfrak{su}(n) $ .*

-   Теорема Кэли для алгебр Ли. Изоморфизмы  $ \mathbb R $ -алгебр Ли:  $ \Biggl(\!\begin{align}\mathbb R^3\!&\to\mathfrak{so}(3)\\\biggl(\begin{smallmatrix}\beta\\\gamma\\\delta\end{smallmatrix}\biggr)\!&\mapsto\!\biggl(\begin{smallmatrix}0&-\delta&\gamma\\\delta&0&-\beta\\-\gamma&\beta&0\end{smallmatrix}\biggr)\end{align}\!\Biggr) $ ,  $ \Biggl(\!\begin{align}\mathbb R^3\!&\to\mathbb H_\rm{vect}\\\biggl(\begin{smallmatrix}\beta\\\gamma\\\delta\end{smallmatrix}\biggr)\!&\mapsto{\textstyle\frac12}(\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k)\end{align}\!\Biggr) $  и  $ \Biggl(\!\begin{align}\mathbb R^3\!&\to\mathfrak{su}(2)\\\biggl(\begin{smallmatrix}\beta\\\gamma\\\delta\end{smallmatrix}\biggr)\!&\mapsto{\textstyle\frac12}\Bigl(\begin{smallmatrix}\beta\,\rm i&\gamma+\delta\,\rm i\\-\gamma+\delta\,\rm i&-\beta\,\rm i\end{smallmatrix}\Bigr)\end{align}\!\Biggr) $ .

    **Теорема Кэли для алгебр Ли.** *Пусть  $ K $  — поле и  $ \mathfrak g $  —  $ K $ -алгебра Ли; обозначим через  $ {}_K\mathfrak g $  векторное пространство над  $ K $ , получающееся из  $ \mathfrak g $  при
    «забывании» умножения в этой алгебре, и для любых  $ a\in\mathfrak g $  обозначим через  $ \rm{ad}_a $  отображение  $ \biggl(\!\begin{align}\mathfrak g&\to\mathfrak g\\b&\mapsto[a,b]\end{align}\!\biggr) $ ; тогда отображение  $ \biggl(\!\begin{align}\mathfrak g&\to\mathfrak{gl}({}_K\mathfrak g)\\a&\mapsto\rm{ad}_a\end{align}\!\biggr) $ 
    определено корректно и является гомоморфизмом алгебр Ли.*

-   Алгебра Ли дифференцирований  $ K $ -алгебры  $ A $ :  $ \rm{Der}(A)=\{d\in\mathfrak{gl}({}_K\!A)\mid\forall\,a,b\in A\;\bigl(d(a\,b)=d(a)\,b+a\,d(b)\bigr)\} $  — подалгебра алгебры  $ \mathfrak{gl}({}_K\!A) $ .

-   Дифференциров.-е (производная Ли) по вект. полю ( $ M $  — откр. мн.-во в  $ \mathbb R^n $ ,  $ A=\rm C^\infty\!(M,\mathbb R) $ ,  $ v\in\rm C^\infty\!(M,\mathbb R^n) $ ):  $ \biggl(\begin{align}\mathcal L_v\colon A&\to A\\f&\mapsto\textstyle\sum_{i=1}^nv^i\frac{\partial f}{\partial x^i}\end{align}\!\biggr)\!\in\rm{Der}(A) $ .
